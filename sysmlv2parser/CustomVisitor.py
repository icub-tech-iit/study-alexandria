from antlr4 import *
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from SysMLv2Visitor import SysMLv2Visitor

class CustomVisitor(SysMLv2Visitor):
    def __init__(self):
        self.part_definitions = {}

    def visitModel(self, ctx: SysMLv2Parser.ModelContext):
        if ctx.partStmt():
            for part_ctx in ctx.partStmt():
                self.visitPart(part_ctx)
        else:
            print("No parts found in the model")
            self.visitAttribute(ctx.attributeStmt)
        return self.visitChildren(ctx)

    def visitPart(self, ctx: SysMLv2Parser.PartStmtContext):
        part_name = ctx.ID(0).getText()
        parent_name = ctx.ID(1).getText() if len(ctx.ID()) > 1 else None

        print(f"Visiting part: {part_name}" + (f" (inherits from {parent_name})" if parent_name else ""))

        part = self.part_definitions.get(part_name, Element(part_name))
        if parent_name and parent_name in self.part_definitions:
            parent_part = self.part_definitions[parent_name]
            part.inherit_from(parent_part)

        if ctx.partBody():
            for part_body in ctx.partBody():
                for attribute_ctx in part_body.attributeStmt():
                    self.visitAttribute(attribute_ctx, part)
                for nested_part_ctx in part_body.partStmt():
                    self.visitPart(nested_part_ctx)
        elif ctx.overrideBody():
            for override_ctx in ctx.overrideBody():
                self.visitOverride(override_ctx.qualifiedID().getText(), override_ctx, part)

        self.part_definitions[part_name] = part

    def visitAttribute(self, ctx: SysMLv2Parser.AttributeStmtContext, part):
        attribute_name = ctx.ID().getText()
        if ctx.attributeType().arrayType():
            self.visitArray(attribute_name, ctx.attributeType().arrayType().arrayBody(), part)
        else:
            attribute_type = ctx.attributeType().getText()
            default_value = ctx.defaultValue().getText() if ctx.defaultValue() else "None"
            print(f"  Attribute: {attribute_name}, Type: {attribute_type}, Default: {default_value}")

            part.set_parameter(attribute_name, default_value)

    def visitArray(self, attribute_name, ctx: SysMLv2Parser.ArrayBodyContext, part):
        array_dimension = ctx.NUMBER().getText()
        array_type = ctx.attributeType().getText()
        default_value = ctx.defaultValue().getText() if ctx.defaultValue() else "None"
        print(f"  Attribute array: {attribute_name}, Dimension: {array_dimension}, Type: {array_type}, Default: {default_value}")

        part.set_parameter(attribute_name, {"dimension": array_dimension, "type": array_type, "value": default_value})

    def visitOverride(self, attribute_name, ctx: SysMLv2Parser.OverrideBodyContext, part):
        override_value = ctx.defaultValue().getText()
        print(f"  Overriding attribute: {attribute_name}, with value: {override_value}")

        part.set_parameter(attribute_name, override_value)

class Element:
    def __init__(self, name):
        self.name = name
        self.parameters = {}

    def inherit_from(self, parent):
        """Inherit attributes from a parent element unless overridden."""
        for key, value in parent.parameters.items():
            self.parameters.setdefault(key, value)

    def set_parameter(self, key, value):
        """Set or override an attribute."""
        self.parameters[key] = value

    def get_parameter(self, key):
        """Retrieve a parameter value or return 'undefined'."""
        return self.parameters.get(key, "undefined")

    def __repr__(self):
        return f"Element(name='{self.name}', parameters={self.parameters})"


from antlr4 import *
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from SysMLv2Visitor import SysMLv2Visitor

class CustomVisitor(SysMLv2Visitor):
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
        specialization = ctx.ID(1).getText() if len(ctx.ID()) > 1 else None
        if specialization is not None:
            print(f"Visiting part: {part_name} that inherits from: {specialization}")
        else:
            print(f"Visiting part: {part_name}")
        if ctx.partBody():
            for part_body in ctx.partBody():
                for attribute_ctx in part_body.attributeStmt():
                    self.visitAttribute(attribute_ctx)
                for nested_part_ctx in part_body.partStmt():
                    self.visitPart(nested_part_ctx)
        elif ctx.overrideBody():
            for override_ctx in ctx.overrideBody():
                self.visitOVerride(override_ctx.qualifiedID().getText(), override_ctx)
    
    def visitAttribute(self, ctx: SysMLv2Parser.AttributeStmtContext):
        attribute_name = ctx.ID().getText()
        if ctx.attributeType().arrayType():
            self.visitArray(attribute_name, ctx.attributeType().arrayType().arrayBody())
        else:
            attribute_type = ctx.attributeType().getText()
            default_value = ctx.defaultValue().getText() if ctx.defaultValue() else "None"
            print(f"  Attribute: {attribute_name}, Type: {attribute_type}, Default: {default_value}")

    def visitArray(self, attribute_name, ctx: SysMLv2Parser.ArrayBodyContext):
        array_dimension = ctx.NUMBER().getText()
        array_type = ctx.attributeType().getText()
        default_value = ctx.defaultValue().getText() if ctx.defaultValue() else "None"
        print(f"  Attribute array: {attribute_name}, Dimension: {array_dimension}, Type: {array_type}, Default: {default_value}")

    def visitOVerride(self, attribute_name, ctx: SysMLv2Parser.OverrideBodyContext):
        override_value = ctx.defaultValue().getText()
        print(f"  Overriding attribute: {attribute_name}, with value: {override_value}")
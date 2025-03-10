
from antlr4 import *
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from SysMLv2Visitor import SysMLv2Visitor

class CustomVisitor(SysMLv2Visitor):
    def visitModel(self, ctx: SysMLv2Parser.ModelContext):
        for part_ctx in ctx.partStmt():
            self.visitPart(part_ctx)
        return self.visitChildren(ctx)

    def visitPart(self, ctx: SysMLv2Parser.PartStmtContext):
        part_name = ctx.ID().getText()
        print(f"Visiting part: {part_name}")
        if ctx.partBody():
            for attribute_ctx in ctx.partBody().attributeStmt():
                self.visitAttribute(attribute_ctx)
            for nested_part_ctx in ctx.partBody().partStmt():
                self.visitPart(nested_part_ctx)
    
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
        print(f"  Array: {attribute_name}, Dimension: {array_dimension}, Type: {array_type}, Default: {default_value}")

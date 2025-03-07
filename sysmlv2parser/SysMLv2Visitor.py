# Generated from SysMLv2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SysMLv2Parser import SysMLv2Parser
else:
    from SysMLv2Parser import SysMLv2Parser

# This class defines a complete generic visitor for a parse tree produced by SysMLv2Parser.

class SysMLv2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by SysMLv2Parser#partStmt.
    def visitPartStmt(self, ctx:SysMLv2Parser.PartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#partBody.
    def visitPartBody(self, ctx:SysMLv2Parser.PartBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#attributeStmt.
    def visitAttributeStmt(self, ctx:SysMLv2Parser.AttributeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#attributeType.
    def visitAttributeType(self, ctx:SysMLv2Parser.AttributeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#defaultValue.
    def visitDefaultValue(self, ctx:SysMLv2Parser.DefaultValueContext):
        return self.visitChildren(ctx)



del SysMLv2Parser
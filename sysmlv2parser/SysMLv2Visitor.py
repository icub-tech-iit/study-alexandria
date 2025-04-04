# Generated from sysmlv2parser/SysMLv2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SysMLv2Parser import SysMLv2Parser
else:
    from SysMLv2Parser import SysMLv2Parser

# This class defines a complete generic visitor for a parse tree produced by SysMLv2Parser.

class SysMLv2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by SysMLv2Parser#qualifiedID.
    def visitQualifiedID(self, ctx:SysMLv2Parser.QualifiedIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#model.
    def visitModel(self, ctx:SysMLv2Parser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#packageStmt.
    def visitPackageStmt(self, ctx:SysMLv2Parser.PackageStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#importStmt.
    def visitImportStmt(self, ctx:SysMLv2Parser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#partStmt.
    def visitPartStmt(self, ctx:SysMLv2Parser.PartStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#partBody.
    def visitPartBody(self, ctx:SysMLv2Parser.PartBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#overrideBody.
    def visitOverrideBody(self, ctx:SysMLv2Parser.OverrideBodyContext):
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


    # Visit a parse tree produced by SysMLv2Parser#vector.
    def visitVector(self, ctx:SysMLv2Parser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#arrayType.
    def visitArrayType(self, ctx:SysMLv2Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SysMLv2Parser#arrayBody.
    def visitArrayBody(self, ctx:SysMLv2Parser.ArrayBodyContext):
        return self.visitChildren(ctx)



del SysMLv2Parser
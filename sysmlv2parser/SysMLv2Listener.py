# Generated from sysmlv2parser/SysMLv2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SysMLv2Parser import SysMLv2Parser
else:
    from SysMLv2Parser import SysMLv2Parser

# This class defines a complete listener for a parse tree produced by SysMLv2Parser.
class SysMLv2Listener(ParseTreeListener):

    # Enter a parse tree produced by SysMLv2Parser#model.
    def enterModel(self, ctx:SysMLv2Parser.ModelContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#model.
    def exitModel(self, ctx:SysMLv2Parser.ModelContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#importStmt.
    def enterImportStmt(self, ctx:SysMLv2Parser.ImportStmtContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#importStmt.
    def exitImportStmt(self, ctx:SysMLv2Parser.ImportStmtContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#partStmt.
    def enterPartStmt(self, ctx:SysMLv2Parser.PartStmtContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#partStmt.
    def exitPartStmt(self, ctx:SysMLv2Parser.PartStmtContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#partBody.
    def enterPartBody(self, ctx:SysMLv2Parser.PartBodyContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#partBody.
    def exitPartBody(self, ctx:SysMLv2Parser.PartBodyContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#attributeStmt.
    def enterAttributeStmt(self, ctx:SysMLv2Parser.AttributeStmtContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#attributeStmt.
    def exitAttributeStmt(self, ctx:SysMLv2Parser.AttributeStmtContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#attributeType.
    def enterAttributeType(self, ctx:SysMLv2Parser.AttributeTypeContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#attributeType.
    def exitAttributeType(self, ctx:SysMLv2Parser.AttributeTypeContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#defaultValue.
    def enterDefaultValue(self, ctx:SysMLv2Parser.DefaultValueContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#defaultValue.
    def exitDefaultValue(self, ctx:SysMLv2Parser.DefaultValueContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#vector.
    def enterVector(self, ctx:SysMLv2Parser.VectorContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#vector.
    def exitVector(self, ctx:SysMLv2Parser.VectorContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#arrayType.
    def enterArrayType(self, ctx:SysMLv2Parser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#arrayType.
    def exitArrayType(self, ctx:SysMLv2Parser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by SysMLv2Parser#arrayBody.
    def enterArrayBody(self, ctx:SysMLv2Parser.ArrayBodyContext):
        pass

    # Exit a parse tree produced by SysMLv2Parser#arrayBody.
    def exitArrayBody(self, ctx:SysMLv2Parser.ArrayBodyContext):
        pass



del SysMLv2Parser
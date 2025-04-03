# Generated from sysmlv2parser/SysMLv2.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,172,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,1,5,1,36,8,1,10,1,12,1,39,9,1,
        1,1,1,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,4,2,56,8,2,11,2,12,2,57,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        3,4,69,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,4,
        4,83,8,4,11,4,12,4,84,1,4,1,4,1,5,1,5,4,5,91,8,5,11,5,12,5,92,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,103,8,7,1,7,1,7,1,7,1,7,1,7,3,
        7,110,8,7,1,7,1,7,1,7,1,7,3,7,116,8,7,1,7,3,7,119,8,7,1,8,1,8,1,
        8,1,8,1,8,1,8,3,8,127,8,8,1,9,1,9,3,9,131,8,9,1,9,1,9,1,9,3,9,136,
        8,9,1,10,1,10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,166,8,12,1,12,1,12,1,12,1,12,1,12,
        0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,2,0,12,12,26,26,1,0,
        3,4,187,0,26,1,0,0,0,2,37,1,0,0,0,4,50,1,0,0,0,6,61,1,0,0,0,8,66,
        1,0,0,0,10,90,1,0,0,0,12,94,1,0,0,0,14,100,1,0,0,0,16,126,1,0,0,
        0,18,135,1,0,0,0,20,137,1,0,0,0,22,148,1,0,0,0,24,153,1,0,0,0,26,
        31,5,30,0,0,27,28,5,1,0,0,28,30,5,30,0,0,29,27,1,0,0,0,30,33,1,0,
        0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,31,1,0,0,0,34,36,
        3,6,3,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,
        38,45,1,0,0,0,39,37,1,0,0,0,40,44,3,8,4,0,41,44,3,14,7,0,42,44,3,
        4,2,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,47,1,0,0,0,45,
        43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,0,0,
        1,49,3,1,0,0,0,50,51,5,8,0,0,51,52,5,30,0,0,52,55,5,14,0,0,53,56,
        3,14,7,0,54,56,3,8,4,0,55,53,1,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,
        57,55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,5,15,0,0,60,5,1,
        0,0,0,61,62,5,6,0,0,62,63,5,30,0,0,63,64,5,2,0,0,64,65,5,13,0,0,
        65,7,1,0,0,0,66,68,5,7,0,0,67,69,5,11,0,0,68,67,1,0,0,0,68,69,1,
        0,0,0,69,70,1,0,0,0,70,77,5,30,0,0,71,72,5,12,0,0,72,78,5,30,0,0,
        73,74,7,0,0,0,74,75,5,30,0,0,75,76,5,20,0,0,76,78,5,32,0,0,77,71,
        1,0,0,0,77,73,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,82,5,14,0,0,
        80,83,3,10,5,0,81,83,3,12,6,0,82,80,1,0,0,0,82,81,1,0,0,0,83,84,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,15,0,0,
        87,9,1,0,0,0,88,91,3,14,7,0,89,91,3,8,4,0,90,88,1,0,0,0,90,89,1,
        0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,11,1,0,0,0,94,
        95,5,27,0,0,95,96,3,0,0,0,96,97,5,20,0,0,97,98,3,18,9,0,98,99,5,
        13,0,0,99,13,1,0,0,0,100,102,5,9,0,0,101,103,5,11,0,0,102,101,1,
        0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,109,5,30,0,0,105,106,5,
        14,0,0,106,107,3,14,7,0,107,108,5,15,0,0,108,110,1,0,0,0,109,105,
        1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,112,5,12,0,0,112,115,
        3,16,8,0,113,114,5,10,0,0,114,116,3,18,9,0,115,113,1,0,0,0,115,116,
        1,0,0,0,116,118,1,0,0,0,117,119,5,13,0,0,118,117,1,0,0,0,118,119,
        1,0,0,0,119,15,1,0,0,0,120,127,5,21,0,0,121,127,5,22,0,0,122,127,
        5,23,0,0,123,127,5,24,0,0,124,127,3,22,11,0,125,127,5,30,0,0,126,
        120,1,0,0,0,126,121,1,0,0,0,126,122,1,0,0,0,126,123,1,0,0,0,126,
        124,1,0,0,0,126,125,1,0,0,0,127,17,1,0,0,0,128,136,5,31,0,0,129,
        131,7,1,0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,
        136,5,31,0,0,133,136,5,32,0,0,134,136,3,20,10,0,135,128,1,0,0,0,
        135,130,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,19,1,0,0,0,137,
        138,5,18,0,0,138,143,3,18,9,0,139,140,5,5,0,0,140,142,3,18,9,0,141,
        139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,
        146,1,0,0,0,145,143,1,0,0,0,146,147,5,19,0,0,147,21,1,0,0,0,148,
        149,5,25,0,0,149,150,5,14,0,0,150,151,3,24,12,0,151,152,5,15,0,0,
        152,23,1,0,0,0,153,154,5,27,0,0,154,155,5,28,0,0,155,156,5,10,0,
        0,156,157,5,31,0,0,157,158,5,13,0,0,158,159,5,27,0,0,159,160,5,29,
        0,0,160,161,5,12,0,0,161,165,3,16,8,0,162,163,5,16,0,0,163,164,5,
        28,0,0,164,166,5,17,0,0,165,162,1,0,0,0,165,166,1,0,0,0,166,167,
        1,0,0,0,167,168,5,10,0,0,168,169,3,18,9,0,169,170,5,13,0,0,170,25,
        1,0,0,0,21,31,37,43,45,55,57,68,77,82,84,90,92,102,109,115,118,126,
        130,135,143,165
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'::*'", "'-'", "'+'", "','", "'import'", 
                     "'part'", "'package'", "'attribute'", "'default'", 
                     "'def'", "':'", "';'", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'", "'='", "'Integer'", "'String'", "'Real'", 
                     "'Boolean'", "'Array'", "':>'", "':>>'", "'dimensions'", 
                     "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IMPORT", "PART", "PACKAGE", 
                      "ATTRIBUTE", "DEFAULT", "DEF", "COLON", "SEMICOLON", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "LPAREN", 
                      "RPAREN", "EQUALS", "INTEGER", "STRING", "REAL", "BOOLEAN", 
                      "ARRAY", "SPECIALIZE", "OVERRIDE", "DIMENSIONS", "ELEMENTS", 
                      "ID", "NUMBER", "STR", "WS" ]

    RULE_qualifiedID = 0
    RULE_model = 1
    RULE_packageStmt = 2
    RULE_importStmt = 3
    RULE_partStmt = 4
    RULE_partBody = 5
    RULE_overrideBody = 6
    RULE_attributeStmt = 7
    RULE_attributeType = 8
    RULE_defaultValue = 9
    RULE_vector = 10
    RULE_arrayType = 11
    RULE_arrayBody = 12

    ruleNames =  [ "qualifiedID", "model", "packageStmt", "importStmt", 
                   "partStmt", "partBody", "overrideBody", "attributeStmt", 
                   "attributeType", "defaultValue", "vector", "arrayType", 
                   "arrayBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IMPORT=6
    PART=7
    PACKAGE=8
    ATTRIBUTE=9
    DEFAULT=10
    DEF=11
    COLON=12
    SEMICOLON=13
    LBRACE=14
    RBRACE=15
    LBRACK=16
    RBRACK=17
    LPAREN=18
    RPAREN=19
    EQUALS=20
    INTEGER=21
    STRING=22
    REAL=23
    BOOLEAN=24
    ARRAY=25
    SPECIALIZE=26
    OVERRIDE=27
    DIMENSIONS=28
    ELEMENTS=29
    ID=30
    NUMBER=31
    STR=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QualifiedIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.ID)
            else:
                return self.getToken(SysMLv2Parser.ID, i)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_qualifiedID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedID" ):
                listener.enterQualifiedID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedID" ):
                listener.exitQualifiedID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedID" ):
                return visitor.visitQualifiedID(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedID(self):

        localctx = SysMLv2Parser.QualifiedIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_qualifiedID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(SysMLv2Parser.ID)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 27
                self.match(SysMLv2Parser.T__0)
                self.state = 28
                self.match(SysMLv2Parser.ID)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SysMLv2Parser.EOF, 0)

        def importStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.ImportStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.ImportStmtContext,i)


        def partStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.PartStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.PartStmtContext,i)


        def attributeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.AttributeStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.AttributeStmtContext,i)


        def packageStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.PackageStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.PackageStmtContext,i)


        def getRuleIndex(self):
            return SysMLv2Parser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = SysMLv2Parser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 34
                self.importStmt()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 43
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 40
                    self.partStmt()
                    pass
                elif token in [9]:
                    self.state = 41
                    self.attributeStmt()
                    pass
                elif token in [8]:
                    self.state = 42
                    self.packageStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(SysMLv2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(SysMLv2Parser.PACKAGE, 0)

        def ID(self):
            return self.getToken(SysMLv2Parser.ID, 0)

        def LBRACE(self):
            return self.getToken(SysMLv2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def attributeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.AttributeStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.AttributeStmtContext,i)


        def partStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.PartStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.PartStmtContext,i)


        def getRuleIndex(self):
            return SysMLv2Parser.RULE_packageStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageStmt" ):
                listener.enterPackageStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageStmt" ):
                listener.exitPackageStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageStmt" ):
                return visitor.visitPackageStmt(self)
            else:
                return visitor.visitChildren(self)




    def packageStmt(self):

        localctx = SysMLv2Parser.PackageStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_packageStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SysMLv2Parser.PACKAGE)
            self.state = 51
            self.match(SysMLv2Parser.ID)
            self.state = 52
            self.match(SysMLv2Parser.LBRACE)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 53
                    self.attributeStmt()
                    pass
                elif token in [7]:
                    self.state = 54
                    self.partStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==9):
                    break

            self.state = 59
            self.match(SysMLv2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(SysMLv2Parser.IMPORT, 0)

        def ID(self):
            return self.getToken(SysMLv2Parser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(SysMLv2Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = SysMLv2Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SysMLv2Parser.IMPORT)
            self.state = 62
            self.match(SysMLv2Parser.ID)
            self.state = 63
            self.match(SysMLv2Parser.T__1)
            self.state = 64
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PART(self):
            return self.getToken(SysMLv2Parser.PART, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.ID)
            else:
                return self.getToken(SysMLv2Parser.ID, i)

        def LBRACE(self):
            return self.getToken(SysMLv2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def DEF(self):
            return self.getToken(SysMLv2Parser.DEF, 0)

        def EQUALS(self):
            return self.getToken(SysMLv2Parser.EQUALS, 0)

        def STR(self):
            return self.getToken(SysMLv2Parser.STR, 0)

        def partBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.PartBodyContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.PartBodyContext,i)


        def overrideBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.OverrideBodyContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.OverrideBodyContext,i)


        def SPECIALIZE(self):
            return self.getToken(SysMLv2Parser.SPECIALIZE, 0)

        def COLON(self):
            return self.getToken(SysMLv2Parser.COLON, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_partStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartStmt" ):
                listener.enterPartStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartStmt" ):
                listener.exitPartStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartStmt" ):
                return visitor.visitPartStmt(self)
            else:
                return visitor.visitChildren(self)




    def partStmt(self):

        localctx = SysMLv2Parser.PartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_partStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SysMLv2Parser.PART)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 67
                self.match(SysMLv2Parser.DEF)


            self.state = 70
            self.match(SysMLv2Parser.ID)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(SysMLv2Parser.COLON)
                self.state = 72
                self.match(SysMLv2Parser.ID)

            elif la_ == 2:
                self.state = 73
                _la = self._input.LA(1)
                if not(_la==12 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74
                self.match(SysMLv2Parser.ID)
                self.state = 75
                self.match(SysMLv2Parser.EQUALS)
                self.state = 76
                self.match(SysMLv2Parser.STR)


            self.state = 79
            self.match(SysMLv2Parser.LBRACE)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7, 9]:
                    self.state = 80
                    self.partBody()
                    pass
                elif token in [27]:
                    self.state = 81
                    self.overrideBody()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 134218368) != 0)):
                    break

            self.state = 86
            self.match(SysMLv2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.AttributeStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.AttributeStmtContext,i)


        def partStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.PartStmtContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.PartStmtContext,i)


        def getRuleIndex(self):
            return SysMLv2Parser.RULE_partBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartBody" ):
                listener.enterPartBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartBody" ):
                listener.exitPartBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartBody" ):
                return visitor.visitPartBody(self)
            else:
                return visitor.visitChildren(self)




    def partBody(self):

        localctx = SysMLv2Parser.PartBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_partBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 90
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9]:
                        self.state = 88
                        self.attributeStmt()
                        pass
                    elif token in [7]:
                        self.state = 89
                        self.partStmt()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 92 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OverrideBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OVERRIDE(self):
            return self.getToken(SysMLv2Parser.OVERRIDE, 0)

        def qualifiedID(self):
            return self.getTypedRuleContext(SysMLv2Parser.QualifiedIDContext,0)


        def EQUALS(self):
            return self.getToken(SysMLv2Parser.EQUALS, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(SysMLv2Parser.DefaultValueContext,0)


        def SEMICOLON(self):
            return self.getToken(SysMLv2Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_overrideBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverrideBody" ):
                listener.enterOverrideBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverrideBody" ):
                listener.exitOverrideBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOverrideBody" ):
                return visitor.visitOverrideBody(self)
            else:
                return visitor.visitChildren(self)




    def overrideBody(self):

        localctx = SysMLv2Parser.OverrideBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_overrideBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 95
            self.qualifiedID()
            self.state = 96
            self.match(SysMLv2Parser.EQUALS)
            self.state = 97
            self.defaultValue()
            self.state = 98
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTRIBUTE(self):
            return self.getToken(SysMLv2Parser.ATTRIBUTE, 0)

        def ID(self):
            return self.getToken(SysMLv2Parser.ID, 0)

        def COLON(self):
            return self.getToken(SysMLv2Parser.COLON, 0)

        def attributeType(self):
            return self.getTypedRuleContext(SysMLv2Parser.AttributeTypeContext,0)


        def DEF(self):
            return self.getToken(SysMLv2Parser.DEF, 0)

        def LBRACE(self):
            return self.getToken(SysMLv2Parser.LBRACE, 0)

        def attributeStmt(self):
            return self.getTypedRuleContext(SysMLv2Parser.AttributeStmtContext,0)


        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def DEFAULT(self):
            return self.getToken(SysMLv2Parser.DEFAULT, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(SysMLv2Parser.DefaultValueContext,0)


        def SEMICOLON(self):
            return self.getToken(SysMLv2Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_attributeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeStmt" ):
                listener.enterAttributeStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeStmt" ):
                listener.exitAttributeStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeStmt" ):
                return visitor.visitAttributeStmt(self)
            else:
                return visitor.visitChildren(self)




    def attributeStmt(self):

        localctx = SysMLv2Parser.AttributeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 101
                self.match(SysMLv2Parser.DEF)


            self.state = 104
            self.match(SysMLv2Parser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 105
                self.match(SysMLv2Parser.LBRACE)
                self.state = 106
                self.attributeStmt()
                self.state = 107
                self.match(SysMLv2Parser.RBRACE)


            self.state = 111
            self.match(SysMLv2Parser.COLON)
            self.state = 112
            self.attributeType()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 113
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 114
                self.defaultValue()


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 117
                self.match(SysMLv2Parser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SysMLv2Parser.INTEGER, 0)

        def STRING(self):
            return self.getToken(SysMLv2Parser.STRING, 0)

        def REAL(self):
            return self.getToken(SysMLv2Parser.REAL, 0)

        def BOOLEAN(self):
            return self.getToken(SysMLv2Parser.BOOLEAN, 0)

        def arrayType(self):
            return self.getTypedRuleContext(SysMLv2Parser.ArrayTypeContext,0)


        def ID(self):
            return self.getToken(SysMLv2Parser.ID, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_attributeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeType" ):
                listener.enterAttributeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeType" ):
                listener.exitAttributeType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeType" ):
                return visitor.visitAttributeType(self)
            else:
                return visitor.visitChildren(self)




    def attributeType(self):

        localctx = SysMLv2Parser.AttributeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributeType)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.arrayType()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.match(SysMLv2Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SysMLv2Parser.NUMBER, 0)

        def STR(self):
            return self.getToken(SysMLv2Parser.STR, 0)

        def vector(self):
            return self.getTypedRuleContext(SysMLv2Parser.VectorContext,0)


        def getRuleIndex(self):
            return SysMLv2Parser.RULE_defaultValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValue" ):
                listener.enterDefaultValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValue" ):
                listener.exitDefaultValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultValue" ):
                return visitor.visitDefaultValue(self)
            else:
                return visitor.visitChildren(self)




    def defaultValue(self):

        localctx = SysMLv2Parser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_defaultValue)
        self._la = 0 # Token type
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3 or _la==4:
                    self.state = 129
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 132
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(SysMLv2Parser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.vector()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SysMLv2Parser.LPAREN, 0)

        def defaultValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SysMLv2Parser.DefaultValueContext)
            else:
                return self.getTypedRuleContext(SysMLv2Parser.DefaultValueContext,i)


        def RPAREN(self):
            return self.getToken(SysMLv2Parser.RPAREN, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = SysMLv2Parser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(SysMLv2Parser.LPAREN)
            self.state = 138
            self.defaultValue()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 139
                self.match(SysMLv2Parser.T__4)
                self.state = 140
                self.defaultValue()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(SysMLv2Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(SysMLv2Parser.ARRAY, 0)

        def LBRACE(self):
            return self.getToken(SysMLv2Parser.LBRACE, 0)

        def arrayBody(self):
            return self.getTypedRuleContext(SysMLv2Parser.ArrayBodyContext,0)


        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = SysMLv2Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(SysMLv2Parser.ARRAY)
            self.state = 149
            self.match(SysMLv2Parser.LBRACE)
            self.state = 150
            self.arrayBody()
            self.state = 151
            self.match(SysMLv2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OVERRIDE(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.OVERRIDE)
            else:
                return self.getToken(SysMLv2Parser.OVERRIDE, i)

        def DIMENSIONS(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.DIMENSIONS)
            else:
                return self.getToken(SysMLv2Parser.DIMENSIONS, i)

        def DEFAULT(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.DEFAULT)
            else:
                return self.getToken(SysMLv2Parser.DEFAULT, i)

        def NUMBER(self):
            return self.getToken(SysMLv2Parser.NUMBER, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.SEMICOLON)
            else:
                return self.getToken(SysMLv2Parser.SEMICOLON, i)

        def ELEMENTS(self):
            return self.getToken(SysMLv2Parser.ELEMENTS, 0)

        def COLON(self):
            return self.getToken(SysMLv2Parser.COLON, 0)

        def attributeType(self):
            return self.getTypedRuleContext(SysMLv2Parser.AttributeTypeContext,0)


        def defaultValue(self):
            return self.getTypedRuleContext(SysMLv2Parser.DefaultValueContext,0)


        def LBRACK(self):
            return self.getToken(SysMLv2Parser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(SysMLv2Parser.RBRACK, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_arrayBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayBody" ):
                listener.enterArrayBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayBody" ):
                listener.exitArrayBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayBody" ):
                return visitor.visitArrayBody(self)
            else:
                return visitor.visitChildren(self)




    def arrayBody(self):

        localctx = SysMLv2Parser.ArrayBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 154
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 155
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 156
            self.match(SysMLv2Parser.NUMBER)
            self.state = 157
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 158
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 159
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 160
            self.match(SysMLv2Parser.COLON)
            self.state = 161
            self.attributeType()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 162
                self.match(SysMLv2Parser.LBRACK)
                self.state = 163
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 164
                self.match(SysMLv2Parser.RBRACK)


            self.state = 167
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 168
            self.defaultValue()
            self.state = 169
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        4,1,35,182,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,1,5,1,38,8,1,10,1,12,1,
        41,9,1,1,1,1,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,2,1,2,1,
        2,1,2,1,2,4,2,58,8,2,11,2,12,2,59,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,3,4,71,8,4,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,4,4,
        83,8,4,11,4,12,4,84,1,4,1,4,1,4,3,4,90,8,4,1,5,1,5,1,5,4,5,95,8,
        5,11,5,12,5,96,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,107,8,7,1,7,1,
        7,1,7,1,7,1,7,3,7,114,8,7,1,7,1,7,1,7,1,7,3,7,120,8,7,1,7,3,7,123,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,131,8,8,1,9,1,9,3,9,135,8,9,1,9,
        1,9,1,9,1,9,3,9,141,8,9,1,10,1,10,1,11,1,11,1,11,1,11,5,11,149,8,
        11,10,11,12,11,152,9,11,1,11,3,11,155,8,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,176,8,13,1,13,1,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,0,3,2,0,11,11,28,28,1,0,3,4,1,0,25,26,
        200,0,28,1,0,0,0,2,39,1,0,0,0,4,52,1,0,0,0,6,63,1,0,0,0,8,68,1,0,
        0,0,10,94,1,0,0,0,12,98,1,0,0,0,14,104,1,0,0,0,16,130,1,0,0,0,18,
        140,1,0,0,0,20,142,1,0,0,0,22,144,1,0,0,0,24,158,1,0,0,0,26,163,
        1,0,0,0,28,33,5,32,0,0,29,30,5,1,0,0,30,32,5,32,0,0,31,29,1,0,0,
        0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,0,35,33,1,
        0,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,
        40,1,0,0,0,40,47,1,0,0,0,41,39,1,0,0,0,42,46,3,8,4,0,43,46,3,14,
        7,0,44,46,3,4,2,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,49,
        1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,
        50,51,5,0,0,1,51,3,1,0,0,0,52,53,5,7,0,0,53,54,5,32,0,0,54,57,5,
        13,0,0,55,58,3,14,7,0,56,58,3,8,4,0,57,55,1,0,0,0,57,56,1,0,0,0,
        58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,
        14,0,0,62,5,1,0,0,0,63,64,5,5,0,0,64,65,5,32,0,0,65,66,5,2,0,0,66,
        67,5,12,0,0,67,7,1,0,0,0,68,70,5,6,0,0,69,71,5,10,0,0,70,69,1,0,
        0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,77,5,32,0,0,73,74,5,11,0,0,74,
        78,5,32,0,0,75,76,7,0,0,0,76,78,5,32,0,0,77,73,1,0,0,0,77,75,1,0,
        0,0,77,78,1,0,0,0,78,89,1,0,0,0,79,82,5,13,0,0,80,83,3,10,5,0,81,
        83,3,12,6,0,82,80,1,0,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,
        0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,14,0,0,87,90,1,0,0,0,88,
        90,5,12,0,0,89,79,1,0,0,0,89,88,1,0,0,0,90,9,1,0,0,0,91,95,3,14,
        7,0,92,95,3,8,4,0,93,95,5,33,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,
        93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,11,1,0,0,
        0,98,99,5,29,0,0,99,100,3,0,0,0,100,101,5,19,0,0,101,102,3,18,9,
        0,102,103,5,12,0,0,103,13,1,0,0,0,104,106,5,8,0,0,105,107,5,10,0,
        0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,113,5,32,0,
        0,109,110,5,13,0,0,110,111,3,14,7,0,111,112,5,14,0,0,112,114,1,0,
        0,0,113,109,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,11,
        0,0,116,119,3,16,8,0,117,118,5,9,0,0,118,120,3,18,9,0,119,117,1,
        0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,123,5,12,0,0,122,121,1,
        0,0,0,122,123,1,0,0,0,123,15,1,0,0,0,124,131,5,21,0,0,125,131,5,
        22,0,0,126,131,5,23,0,0,127,131,5,24,0,0,128,131,3,24,12,0,129,131,
        5,32,0,0,130,124,1,0,0,0,130,125,1,0,0,0,130,126,1,0,0,0,130,127,
        1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,17,1,0,0,0,132,141,5,
        33,0,0,133,135,7,1,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,
        0,0,0,136,141,5,33,0,0,137,141,5,34,0,0,138,141,3,22,11,0,139,141,
        3,20,10,0,140,132,1,0,0,0,140,134,1,0,0,0,140,137,1,0,0,0,140,138,
        1,0,0,0,140,139,1,0,0,0,141,19,1,0,0,0,142,143,7,2,0,0,143,21,1,
        0,0,0,144,145,5,17,0,0,145,150,3,18,9,0,146,147,5,20,0,0,147,149,
        3,18,9,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,
        1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,153,155,5,20,0,0,154,153,
        1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,5,18,0,0,157,23,
        1,0,0,0,158,159,5,27,0,0,159,160,5,13,0,0,160,161,3,26,13,0,161,
        162,5,14,0,0,162,25,1,0,0,0,163,164,5,29,0,0,164,165,5,30,0,0,165,
        166,5,9,0,0,166,167,5,33,0,0,167,168,5,12,0,0,168,169,5,29,0,0,169,
        170,5,31,0,0,170,171,5,11,0,0,171,175,3,16,8,0,172,173,5,15,0,0,
        173,174,5,30,0,0,174,176,5,16,0,0,175,172,1,0,0,0,175,176,1,0,0,
        0,176,177,1,0,0,0,177,178,5,9,0,0,178,179,3,18,9,0,179,180,5,12,
        0,0,180,27,1,0,0,0,23,33,39,45,47,57,59,70,77,82,84,89,94,96,106,
        113,119,122,130,134,140,150,154,175
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'::*'", "'-'", "'+'", "'import'", 
                     "'part'", "'package'", "'attribute'", "'default'", 
                     "'def'", "':'", "';'", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'", "'='", "','", "'Integer'", "'String'", 
                     "'Real'", "'Boolean'", "'false'", "'true'", "'Array'", 
                     "':>'", "':>>'", "'dimensions'", "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IMPORT", "PART", "PACKAGE", "ATTRIBUTE", 
                      "DEFAULT", "DEF", "COLON", "SEMICOLON", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "LPAREN", "RPAREN", 
                      "EQUALS", "COMMA", "INTEGER", "STRING", "REAL", "BOOLEAN", 
                      "FALSE", "TRUE", "ARRAY", "SPECIALIZE", "OVERRIDE", 
                      "DIMENSIONS", "ELEMENTS", "ID", "NUMBER", "STR", "WS" ]

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
    RULE_bool = 10
    RULE_vector = 11
    RULE_arrayType = 12
    RULE_arrayBody = 13

    ruleNames =  [ "qualifiedID", "model", "packageStmt", "importStmt", 
                   "partStmt", "partBody", "overrideBody", "attributeStmt", 
                   "attributeType", "defaultValue", "bool", "vector", "arrayType", 
                   "arrayBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IMPORT=5
    PART=6
    PACKAGE=7
    ATTRIBUTE=8
    DEFAULT=9
    DEF=10
    COLON=11
    SEMICOLON=12
    LBRACE=13
    RBRACE=14
    LBRACK=15
    RBRACK=16
    LPAREN=17
    RPAREN=18
    EQUALS=19
    COMMA=20
    INTEGER=21
    STRING=22
    REAL=23
    BOOLEAN=24
    FALSE=25
    TRUE=26
    ARRAY=27
    SPECIALIZE=28
    OVERRIDE=29
    DIMENSIONS=30
    ELEMENTS=31
    ID=32
    NUMBER=33
    STR=34
    WS=35

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
            self.state = 28
            self.match(SysMLv2Parser.ID)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 29
                self.match(SysMLv2Parser.T__0)
                self.state = 30
                self.match(SysMLv2Parser.ID)
                self.state = 35
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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 36
                self.importStmt()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 42
                    self.partStmt()
                    pass
                elif token in [8]:
                    self.state = 43
                    self.attributeStmt()
                    pass
                elif token in [7]:
                    self.state = 44
                    self.packageStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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
            self.state = 52
            self.match(SysMLv2Parser.PACKAGE)
            self.state = 53
            self.match(SysMLv2Parser.ID)
            self.state = 54
            self.match(SysMLv2Parser.LBRACE)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 55
                    self.attributeStmt()
                    pass
                elif token in [6]:
                    self.state = 56
                    self.partStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==8):
                    break

            self.state = 61
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
            self.state = 63
            self.match(SysMLv2Parser.IMPORT)
            self.state = 64
            self.match(SysMLv2Parser.ID)
            self.state = 65
            self.match(SysMLv2Parser.T__1)
            self.state = 66
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

        def SEMICOLON(self):
            return self.getToken(SysMLv2Parser.SEMICOLON, 0)

        def DEF(self):
            return self.getToken(SysMLv2Parser.DEF, 0)

        def SPECIALIZE(self):
            return self.getToken(SysMLv2Parser.SPECIALIZE, 0)

        def COLON(self):
            return self.getToken(SysMLv2Parser.COLON, 0)

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
            self.state = 68
            self.match(SysMLv2Parser.PART)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 69
                self.match(SysMLv2Parser.DEF)


            self.state = 72
            self.match(SysMLv2Parser.ID)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(SysMLv2Parser.COLON)
                self.state = 74
                self.match(SysMLv2Parser.ID)

            elif la_ == 2:
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==11 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76
                self.match(SysMLv2Parser.ID)


            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 79
                self.match(SysMLv2Parser.LBRACE)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 82
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6, 8, 33]:
                        self.state = 80
                        self.partBody()
                        pass
                    elif token in [29]:
                        self.state = 81
                        self.overrideBody()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9126805824) != 0)):
                        break

                self.state = 86
                self.match(SysMLv2Parser.RBRACE)
                pass
            elif token in [12]:
                self.state = 88
                self.match(SysMLv2Parser.SEMICOLON)
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


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.NUMBER)
            else:
                return self.getToken(SysMLv2Parser.NUMBER, i)

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
            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 94
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 91
                        self.attributeStmt()
                        pass
                    elif token in [6]:
                        self.state = 92
                        self.partStmt()
                        pass
                    elif token in [33]:
                        self.state = 93
                        self.match(SysMLv2Parser.NUMBER)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 96 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 98
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 99
            self.qualifiedID()
            self.state = 100
            self.match(SysMLv2Parser.EQUALS)
            self.state = 101
            self.defaultValue()
            self.state = 102
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
            self.state = 104
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 105
                self.match(SysMLv2Parser.DEF)


            self.state = 108
            self.match(SysMLv2Parser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 109
                self.match(SysMLv2Parser.LBRACE)
                self.state = 110
                self.attributeStmt()
                self.state = 111
                self.match(SysMLv2Parser.RBRACE)


            self.state = 115
            self.match(SysMLv2Parser.COLON)
            self.state = 116
            self.attributeType()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 117
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 118
                self.defaultValue()


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 121
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
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.arrayType()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
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


        def bool_(self):
            return self.getTypedRuleContext(SysMLv2Parser.BoolContext,0)


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
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3 or _la==4:
                    self.state = 133
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 136
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(SysMLv2Parser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.vector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.bool_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SysMLv2Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SysMLv2Parser.FALSE, 0)

        def getRuleIndex(self):
            return SysMLv2Parser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = SysMLv2Parser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.COMMA)
            else:
                return self.getToken(SysMLv2Parser.COMMA, i)

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
        self.enterRule(localctx, 22, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(SysMLv2Parser.LPAREN)
            self.state = 145
            self.defaultValue()
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 146
                    self.match(SysMLv2Parser.COMMA)
                    self.state = 147
                    self.defaultValue() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 153
                self.match(SysMLv2Parser.COMMA)


            self.state = 156
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
        self.enterRule(localctx, 24, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(SysMLv2Parser.ARRAY)
            self.state = 159
            self.match(SysMLv2Parser.LBRACE)
            self.state = 160
            self.arrayBody()
            self.state = 161
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
        self.enterRule(localctx, 26, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 164
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 165
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 166
            self.match(SysMLv2Parser.NUMBER)
            self.state = 167
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 168
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 169
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 170
            self.match(SysMLv2Parser.COLON)
            self.state = 171
            self.attributeType()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 172
                self.match(SysMLv2Parser.LBRACK)
                self.state = 173
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 174
                self.match(SysMLv2Parser.RBRACK)


            self.state = 177
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 178
            self.defaultValue()
            self.state = 179
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






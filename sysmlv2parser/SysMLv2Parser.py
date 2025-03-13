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
        4,1,32,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,1,1,5,1,
        41,8,1,10,1,12,1,44,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,3,3,
        55,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,4,3,69,
        8,3,11,3,12,3,70,1,3,1,3,1,4,1,4,4,4,77,8,4,11,4,12,4,78,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,3,6,89,8,6,1,6,1,6,1,6,1,6,1,6,3,6,96,8,
        6,1,6,1,6,1,6,1,6,3,6,102,8,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,113,8,7,1,8,1,8,3,8,117,8,8,1,8,1,8,1,8,3,8,122,8,8,1,
        9,1,9,1,9,1,9,5,9,128,8,9,10,9,12,9,131,9,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,152,8,11,1,11,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,
        10,12,14,16,18,20,22,0,1,1,0,3,4,171,0,24,1,0,0,0,2,35,1,0,0,0,4,
        47,1,0,0,0,6,52,1,0,0,0,8,76,1,0,0,0,10,80,1,0,0,0,12,86,1,0,0,0,
        14,112,1,0,0,0,16,121,1,0,0,0,18,123,1,0,0,0,20,134,1,0,0,0,22,139,
        1,0,0,0,24,29,5,29,0,0,25,26,5,1,0,0,26,28,5,29,0,0,27,25,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,29,1,
        0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,
        36,1,0,0,0,36,42,1,0,0,0,37,35,1,0,0,0,38,41,3,6,3,0,39,41,3,12,
        6,0,40,38,1,0,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,
        1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,0,0,1,46,3,1,0,0,0,47,
        48,5,6,0,0,48,49,5,29,0,0,49,50,5,2,0,0,50,51,5,12,0,0,51,5,1,0,
        0,0,52,54,5,7,0,0,53,55,5,10,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,
        56,1,0,0,0,56,63,5,29,0,0,57,58,5,11,0,0,58,64,5,29,0,0,59,60,5,
        25,0,0,60,61,5,29,0,0,61,62,5,19,0,0,62,64,5,31,0,0,63,57,1,0,0,
        0,63,59,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,68,5,13,0,0,66,69,
        3,8,4,0,67,69,3,10,5,0,68,66,1,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,
        70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,14,0,0,73,7,1,
        0,0,0,74,77,3,12,6,0,75,77,3,6,3,0,76,74,1,0,0,0,76,75,1,0,0,0,77,
        78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,9,1,0,0,0,80,81,5,26,0,
        0,81,82,3,0,0,0,82,83,5,19,0,0,83,84,3,16,8,0,84,85,5,12,0,0,85,
        11,1,0,0,0,86,88,5,8,0,0,87,89,5,10,0,0,88,87,1,0,0,0,88,89,1,0,
        0,0,89,90,1,0,0,0,90,95,5,29,0,0,91,92,5,13,0,0,92,93,3,12,6,0,93,
        94,5,14,0,0,94,96,1,0,0,0,95,91,1,0,0,0,95,96,1,0,0,0,96,97,1,0,
        0,0,97,98,5,11,0,0,98,101,3,14,7,0,99,100,5,9,0,0,100,102,3,16,8,
        0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,5,12,0,
        0,104,103,1,0,0,0,104,105,1,0,0,0,105,13,1,0,0,0,106,113,5,20,0,
        0,107,113,5,21,0,0,108,113,5,22,0,0,109,113,5,23,0,0,110,113,3,20,
        10,0,111,113,5,29,0,0,112,106,1,0,0,0,112,107,1,0,0,0,112,108,1,
        0,0,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,15,1,0,
        0,0,114,122,5,30,0,0,115,117,7,0,0,0,116,115,1,0,0,0,116,117,1,0,
        0,0,117,118,1,0,0,0,118,122,5,30,0,0,119,122,5,31,0,0,120,122,3,
        18,9,0,121,114,1,0,0,0,121,116,1,0,0,0,121,119,1,0,0,0,121,120,1,
        0,0,0,122,17,1,0,0,0,123,124,5,17,0,0,124,129,3,16,8,0,125,126,5,
        5,0,0,126,128,3,16,8,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,
        0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,
        18,0,0,133,19,1,0,0,0,134,135,5,24,0,0,135,136,5,13,0,0,136,137,
        3,22,11,0,137,138,5,14,0,0,138,21,1,0,0,0,139,140,5,26,0,0,140,141,
        5,27,0,0,141,142,5,9,0,0,142,143,5,30,0,0,143,144,5,12,0,0,144,145,
        5,26,0,0,145,146,5,28,0,0,146,147,5,11,0,0,147,151,3,14,7,0,148,
        149,5,15,0,0,149,150,5,27,0,0,150,152,5,16,0,0,151,148,1,0,0,0,151,
        152,1,0,0,0,152,153,1,0,0,0,153,154,5,9,0,0,154,155,3,16,8,0,155,
        156,5,12,0,0,156,23,1,0,0,0,19,29,35,40,42,54,63,68,70,76,78,88,
        95,101,104,112,116,121,129,151
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'::*'", "'-'", "'+'", "','", "'import'", 
                     "'part'", "'attribute'", "'default'", "'def'", "':'", 
                     "';'", "'{'", "'}'", "'['", "']'", "'('", "')'", "'='", 
                     "'Integer'", "'String'", "'Real'", "'Boolean'", "'Array'", 
                     "':>'", "':>>'", "'dimensions'", "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IMPORT", "PART", "ATTRIBUTE", 
                      "DEFAULT", "DEF", "COLON", "SEMICOLON", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "LPAREN", "RPAREN", 
                      "EQUALS", "INTEGER", "STRING", "REAL", "BOOLEAN", 
                      "ARRAY", "SPECIALIZE", "OVERRIDE", "DIMENSIONS", "ELEMENTS", 
                      "ID", "NUMBER", "STR", "WS" ]

    RULE_qualifiedID = 0
    RULE_model = 1
    RULE_importStmt = 2
    RULE_partStmt = 3
    RULE_partBody = 4
    RULE_overrideBody = 5
    RULE_attributeStmt = 6
    RULE_attributeType = 7
    RULE_defaultValue = 8
    RULE_vector = 9
    RULE_arrayType = 10
    RULE_arrayBody = 11

    ruleNames =  [ "qualifiedID", "model", "importStmt", "partStmt", "partBody", 
                   "overrideBody", "attributeStmt", "attributeType", "defaultValue", 
                   "vector", "arrayType", "arrayBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IMPORT=6
    PART=7
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
    INTEGER=20
    STRING=21
    REAL=22
    BOOLEAN=23
    ARRAY=24
    SPECIALIZE=25
    OVERRIDE=26
    DIMENSIONS=27
    ELEMENTS=28
    ID=29
    NUMBER=30
    STR=31
    WS=32

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




    def qualifiedID(self):

        localctx = SysMLv2Parser.QualifiedIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_qualifiedID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SysMLv2Parser.ID)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 25
                self.match(SysMLv2Parser.T__0)
                self.state = 26
                self.match(SysMLv2Parser.ID)
                self.state = 31
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


        def getRuleIndex(self):
            return SysMLv2Parser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)




    def model(self):

        localctx = SysMLv2Parser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 32
                self.importStmt()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 40
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 38
                    self.partStmt()
                    pass
                elif token in [8]:
                    self.state = 39
                    self.attributeStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(SysMLv2Parser.EOF)
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




    def importStmt(self):

        localctx = SysMLv2Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(SysMLv2Parser.IMPORT)
            self.state = 48
            self.match(SysMLv2Parser.ID)
            self.state = 49
            self.match(SysMLv2Parser.T__1)
            self.state = 50
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

        def SPECIALIZE(self):
            return self.getToken(SysMLv2Parser.SPECIALIZE, 0)

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




    def partStmt(self):

        localctx = SysMLv2Parser.PartStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_partStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SysMLv2Parser.PART)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 53
                self.match(SysMLv2Parser.DEF)


            self.state = 56
            self.match(SysMLv2Parser.ID)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 57
                self.match(SysMLv2Parser.COLON)
                self.state = 58
                self.match(SysMLv2Parser.ID)
                pass
            elif token in [25]:
                self.state = 59
                self.match(SysMLv2Parser.SPECIALIZE)
                self.state = 60
                self.match(SysMLv2Parser.ID)
                self.state = 61
                self.match(SysMLv2Parser.EQUALS)
                self.state = 62
                self.match(SysMLv2Parser.STR)
                pass
            elif token in [13]:
                pass
            else:
                pass
            self.state = 65
            self.match(SysMLv2Parser.LBRACE)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7, 8]:
                    self.state = 66
                    self.partBody()
                    pass
                elif token in [26]:
                    self.state = 67
                    self.overrideBody()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67109248) != 0)):
                    break

            self.state = 72
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




    def partBody(self):

        localctx = SysMLv2Parser.PartBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_partBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 76
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 74
                        self.attributeStmt()
                        pass
                    elif token in [7]:
                        self.state = 75
                        self.partStmt()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 78 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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




    def overrideBody(self):

        localctx = SysMLv2Parser.OverrideBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_overrideBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 81
            self.qualifiedID()
            self.state = 82
            self.match(SysMLv2Parser.EQUALS)
            self.state = 83
            self.defaultValue()
            self.state = 84
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




    def attributeStmt(self):

        localctx = SysMLv2Parser.AttributeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 87
                self.match(SysMLv2Parser.DEF)


            self.state = 90
            self.match(SysMLv2Parser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 91
                self.match(SysMLv2Parser.LBRACE)
                self.state = 92
                self.attributeStmt()
                self.state = 93
                self.match(SysMLv2Parser.RBRACE)


            self.state = 97
            self.match(SysMLv2Parser.COLON)
            self.state = 98
            self.attributeType()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 99
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 100
                self.defaultValue()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 103
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




    def attributeType(self):

        localctx = SysMLv2Parser.AttributeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributeType)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
                self.arrayType()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 111
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




    def defaultValue(self):

        localctx = SysMLv2Parser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_defaultValue)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3 or _la==4:
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 118
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(SysMLv2Parser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
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




    def vector(self):

        localctx = SysMLv2Parser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(SysMLv2Parser.LPAREN)
            self.state = 124
            self.defaultValue()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 125
                self.match(SysMLv2Parser.T__4)
                self.state = 126
                self.defaultValue()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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




    def arrayType(self):

        localctx = SysMLv2Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(SysMLv2Parser.ARRAY)
            self.state = 135
            self.match(SysMLv2Parser.LBRACE)
            self.state = 136
            self.arrayBody()
            self.state = 137
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




    def arrayBody(self):

        localctx = SysMLv2Parser.ArrayBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 140
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 141
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 142
            self.match(SysMLv2Parser.NUMBER)
            self.state = 143
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 144
            self.match(SysMLv2Parser.OVERRIDE)
            self.state = 145
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 146
            self.match(SysMLv2Parser.COLON)
            self.state = 147
            self.attributeType()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 148
                self.match(SysMLv2Parser.LBRACK)
                self.state = 149
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 150
                self.match(SysMLv2Parser.RBRACK)


            self.state = 153
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 154
            self.defaultValue()
            self.state = 155
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        4,1,30,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,3,2,43,8,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,3,1,3,4,3,
        56,8,3,11,3,12,3,57,1,4,1,4,3,4,62,8,4,1,4,1,4,1,4,1,4,1,4,3,4,69,
        8,4,1,4,1,4,1,4,1,4,3,4,75,8,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,86,8,5,1,6,1,6,3,6,90,8,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,
        7,1,7,1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,125,8,9,
        1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,2,3,
        142,0,23,1,0,0,0,2,35,1,0,0,0,4,40,1,0,0,0,6,55,1,0,0,0,8,59,1,0,
        0,0,10,85,1,0,0,0,12,94,1,0,0,0,14,96,1,0,0,0,16,107,1,0,0,0,18,
        112,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,
        0,0,23,24,1,0,0,0,24,30,1,0,0,0,25,23,1,0,0,0,26,29,3,4,2,0,27,29,
        3,8,4,0,28,26,1,0,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,
        0,0,35,36,5,5,0,0,36,37,5,27,0,0,37,38,5,1,0,0,38,39,5,11,0,0,39,
        3,1,0,0,0,40,42,5,6,0,0,41,43,5,9,0,0,42,41,1,0,0,0,42,43,1,0,0,
        0,43,44,1,0,0,0,44,47,5,27,0,0,45,46,5,10,0,0,46,48,5,27,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,12,0,0,50,51,3,6,
        3,0,51,52,5,13,0,0,52,5,1,0,0,0,53,56,3,8,4,0,54,56,3,4,2,0,55,53,
        1,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,7,1,0,0,0,59,61,5,7,0,0,60,62,5,9,0,0,61,60,1,0,0,0,61,62,1,0,
        0,0,62,63,1,0,0,0,63,68,5,27,0,0,64,65,5,12,0,0,65,66,3,8,4,0,66,
        67,5,13,0,0,67,69,1,0,0,0,68,64,1,0,0,0,68,69,1,0,0,0,69,70,1,0,
        0,0,70,71,5,10,0,0,71,74,3,10,5,0,72,73,5,8,0,0,73,75,3,12,6,0,74,
        72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,5,11,0,0,77,76,1,0,
        0,0,77,78,1,0,0,0,78,9,1,0,0,0,79,86,5,19,0,0,80,86,5,20,0,0,81,
        86,5,21,0,0,82,86,5,22,0,0,83,86,3,16,8,0,84,86,5,27,0,0,85,79,1,
        0,0,0,85,80,1,0,0,0,85,81,1,0,0,0,85,82,1,0,0,0,85,83,1,0,0,0,85,
        84,1,0,0,0,86,11,1,0,0,0,87,95,5,28,0,0,88,90,7,0,0,0,89,88,1,0,
        0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,95,5,28,0,0,92,95,5,29,0,0,93,
        95,3,14,7,0,94,87,1,0,0,0,94,89,1,0,0,0,94,92,1,0,0,0,94,93,1,0,
        0,0,95,13,1,0,0,0,96,97,5,16,0,0,97,102,3,12,6,0,98,99,5,4,0,0,99,
        101,3,12,6,0,100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,
        103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,17,0,0,106,
        15,1,0,0,0,107,108,5,23,0,0,108,109,5,12,0,0,109,110,3,18,9,0,110,
        111,5,13,0,0,111,17,1,0,0,0,112,113,5,24,0,0,113,114,5,25,0,0,114,
        115,5,8,0,0,115,116,5,28,0,0,116,117,5,11,0,0,117,118,5,24,0,0,118,
        119,5,26,0,0,119,120,5,10,0,0,120,124,3,10,5,0,121,122,5,14,0,0,
        122,123,5,25,0,0,123,125,5,15,0,0,124,121,1,0,0,0,124,125,1,0,0,
        0,125,126,1,0,0,0,126,127,5,8,0,0,127,128,3,12,6,0,128,129,5,11,
        0,0,129,19,1,0,0,0,16,23,28,30,42,47,55,57,61,68,74,77,85,89,94,
        102,124
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::*'", "'-'", "'+'", "','", "'import'", 
                     "'part'", "'attribute'", "'default'", "'def'", "':'", 
                     "';'", "'{'", "'}'", "'['", "']'", "'('", "')'", "'='", 
                     "'Integer'", "'String'", "'Real'", "'Boolean'", "'Array'", 
                     "':>>'", "'dimensions'", "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IMPORT", "PART", "ATTRIBUTE", "DEFAULT", 
                      "DEF", "COLON", "SEMICOLON", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "LPAREN", "RPAREN", "EQUALS", "INTEGER", 
                      "STRING", "REAL", "BOOLEAN", "ARRAY", "SPECIALIZE", 
                      "DIMENSIONS", "ELEMENTS", "ID", "NUMBER", "STR", "WS" ]

    RULE_model = 0
    RULE_importStmt = 1
    RULE_partStmt = 2
    RULE_partBody = 3
    RULE_attributeStmt = 4
    RULE_attributeType = 5
    RULE_defaultValue = 6
    RULE_vector = 7
    RULE_arrayType = 8
    RULE_arrayBody = 9

    ruleNames =  [ "model", "importStmt", "partStmt", "partBody", "attributeStmt", 
                   "attributeType", "defaultValue", "vector", "arrayType", 
                   "arrayBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IMPORT=5
    PART=6
    ATTRIBUTE=7
    DEFAULT=8
    DEF=9
    COLON=10
    SEMICOLON=11
    LBRACE=12
    RBRACE=13
    LBRACK=14
    RBRACK=15
    LPAREN=16
    RPAREN=17
    EQUALS=18
    INTEGER=19
    STRING=20
    REAL=21
    BOOLEAN=22
    ARRAY=23
    SPECIALIZE=24
    DIMENSIONS=25
    ELEMENTS=26
    ID=27
    NUMBER=28
    STR=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 20
                self.importStmt()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 26
                    self.partStmt()
                    pass
                elif token in [7]:
                    self.state = 27
                    self.attributeStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
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
        self.enterRule(localctx, 2, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(SysMLv2Parser.IMPORT)
            self.state = 36
            self.match(SysMLv2Parser.ID)
            self.state = 37
            self.match(SysMLv2Parser.T__0)
            self.state = 38
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

        def partBody(self):
            return self.getTypedRuleContext(SysMLv2Parser.PartBodyContext,0)


        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def DEF(self):
            return self.getToken(SysMLv2Parser.DEF, 0)

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
        self.enterRule(localctx, 4, self.RULE_partStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(SysMLv2Parser.PART)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 41
                self.match(SysMLv2Parser.DEF)


            self.state = 44
            self.match(SysMLv2Parser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 45
                self.match(SysMLv2Parser.COLON)
                self.state = 46
                self.match(SysMLv2Parser.ID)


            self.state = 49
            self.match(SysMLv2Parser.LBRACE)
            self.state = 50
            self.partBody()
            self.state = 51
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
        self.enterRule(localctx, 6, self.RULE_partBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 53
                    self.attributeStmt()
                    pass
                elif token in [6]:
                    self.state = 54
                    self.partStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

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
        self.enterRule(localctx, 8, self.RULE_attributeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 60
                self.match(SysMLv2Parser.DEF)


            self.state = 63
            self.match(SysMLv2Parser.ID)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 64
                self.match(SysMLv2Parser.LBRACE)
                self.state = 65
                self.attributeStmt()
                self.state = 66
                self.match(SysMLv2Parser.RBRACE)


            self.state = 70
            self.match(SysMLv2Parser.COLON)
            self.state = 71
            self.attributeType()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 72
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 73
                self.defaultValue()


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 76
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
        self.enterRule(localctx, 10, self.RULE_attributeType)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.arrayType()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
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
        self.enterRule(localctx, 12, self.RULE_defaultValue)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==3:
                    self.state = 88
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 91
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(SysMLv2Parser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
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
        self.enterRule(localctx, 14, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(SysMLv2Parser.LPAREN)
            self.state = 97
            self.defaultValue()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 98
                self.match(SysMLv2Parser.T__3)
                self.state = 99
                self.defaultValue()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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
        self.enterRule(localctx, 16, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SysMLv2Parser.ARRAY)
            self.state = 108
            self.match(SysMLv2Parser.LBRACE)
            self.state = 109
            self.arrayBody()
            self.state = 110
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

        def SPECIALIZE(self, i:int=None):
            if i is None:
                return self.getTokens(SysMLv2Parser.SPECIALIZE)
            else:
                return self.getToken(SysMLv2Parser.SPECIALIZE, i)

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
        self.enterRule(localctx, 18, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 113
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 114
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 115
            self.match(SysMLv2Parser.NUMBER)
            self.state = 116
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 117
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 118
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 119
            self.match(SysMLv2Parser.COLON)
            self.state = 120
            self.attributeType()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 121
                self.match(SysMLv2Parser.LBRACK)
                self.state = 122
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 123
                self.match(SysMLv2Parser.RBRACK)


            self.state = 126
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 127
            self.defaultValue()
            self.state = 128
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






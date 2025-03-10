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
        4,1,30,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,5,
        0,28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,3,
        2,42,8,2,1,2,1,2,1,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,3,1,3,4,3,55,8,
        3,11,3,12,3,56,1,4,1,4,3,4,61,8,4,1,4,1,4,1,4,1,4,1,4,3,4,68,8,4,
        1,4,3,4,71,8,4,1,5,1,5,1,5,1,5,1,5,3,5,78,8,5,1,6,1,6,3,6,82,8,6,
        1,6,1,6,1,6,3,6,87,8,6,1,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,117,8,9,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,
        12,14,16,18,0,0,131,0,23,1,0,0,0,2,34,1,0,0,0,4,39,1,0,0,0,6,54,
        1,0,0,0,8,58,1,0,0,0,10,77,1,0,0,0,12,86,1,0,0,0,14,88,1,0,0,0,16,
        99,1,0,0,0,18,104,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,
        0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,29,1,0,0,0,25,23,1,0,0,0,26,28,
        3,4,2,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,5,4,
        0,0,35,36,5,26,0,0,36,37,5,1,0,0,37,38,5,10,0,0,38,3,1,0,0,0,39,
        41,5,5,0,0,40,42,5,8,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,
        0,43,46,5,26,0,0,44,45,5,9,0,0,45,47,5,27,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,48,1,0,0,0,48,49,5,11,0,0,49,50,3,6,3,0,50,51,5,12,0,
        0,51,5,1,0,0,0,52,55,3,8,4,0,53,55,3,4,2,0,54,52,1,0,0,0,54,53,1,
        0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,7,1,0,0,0,58,
        60,5,6,0,0,59,61,5,8,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,
        0,62,63,5,26,0,0,63,64,5,9,0,0,64,67,3,10,5,0,65,66,5,7,0,0,66,68,
        3,12,6,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,5,10,0,
        0,70,69,1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,78,5,18,0,0,73,78,
        5,19,0,0,74,78,5,20,0,0,75,78,5,21,0,0,76,78,3,16,8,0,77,72,1,0,
        0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,11,
        1,0,0,0,79,87,5,28,0,0,80,82,5,2,0,0,81,80,1,0,0,0,81,82,1,0,0,0,
        82,83,1,0,0,0,83,87,5,28,0,0,84,87,5,29,0,0,85,87,3,14,7,0,86,79,
        1,0,0,0,86,81,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,13,1,0,0,0,
        88,89,5,15,0,0,89,94,3,12,6,0,90,91,5,3,0,0,91,93,3,12,6,0,92,90,
        1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,
        96,94,1,0,0,0,97,98,5,16,0,0,98,15,1,0,0,0,99,100,5,22,0,0,100,101,
        5,11,0,0,101,102,3,18,9,0,102,103,5,12,0,0,103,17,1,0,0,0,104,105,
        5,23,0,0,105,106,5,24,0,0,106,107,5,7,0,0,107,108,5,28,0,0,108,109,
        5,10,0,0,109,110,5,23,0,0,110,111,5,25,0,0,111,112,5,9,0,0,112,116,
        3,10,5,0,113,114,5,13,0,0,114,115,5,24,0,0,115,117,5,14,0,0,116,
        113,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,7,0,0,119,
        120,3,12,6,0,120,121,5,10,0,0,121,19,1,0,0,0,14,23,29,41,46,54,56,
        60,67,70,77,81,86,94,116
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::*'", "'-'", "','", "'import'", "'part'", 
                     "'attribute'", "'default'", "'def'", "':'", "';'", 
                     "'{'", "'}'", "'['", "']'", "'('", "')'", "'='", "'Integer'", 
                     "'String'", "'Real'", "'Boolean'", "'Array'", "':>>'", 
                     "'dimensions'", "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IMPORT", "PART", "ATTRIBUTE", "DEFAULT", "DEF", "COLON", 
                      "SEMICOLON", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "LPAREN", "RPAREN", "EQUALS", "INTEGER", "STRING", 
                      "REAL", "BOOLEAN", "ARRAY", "SPECIALIZE", "DIMENSIONS", 
                      "ELEMENTS", "ID", "SPECIALIZATION", "NUMBER", "STR", 
                      "WS" ]

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
    IMPORT=4
    PART=5
    ATTRIBUTE=6
    DEFAULT=7
    DEF=8
    COLON=9
    SEMICOLON=10
    LBRACE=11
    RBRACE=12
    LBRACK=13
    RBRACK=14
    LPAREN=15
    RPAREN=16
    EQUALS=17
    INTEGER=18
    STRING=19
    REAL=20
    BOOLEAN=21
    ARRAY=22
    SPECIALIZE=23
    DIMENSIONS=24
    ELEMENTS=25
    ID=26
    SPECIALIZATION=27
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
            while _la==4:
                self.state = 20
                self.importStmt()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 26
                self.partStmt()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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
            self.state = 34
            self.match(SysMLv2Parser.IMPORT)
            self.state = 35
            self.match(SysMLv2Parser.ID)
            self.state = 36
            self.match(SysMLv2Parser.T__0)
            self.state = 37
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

        def ID(self):
            return self.getToken(SysMLv2Parser.ID, 0)

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

        def SPECIALIZATION(self):
            return self.getToken(SysMLv2Parser.SPECIALIZATION, 0)

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
            self.state = 39
            self.match(SysMLv2Parser.PART)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 40
                self.match(SysMLv2Parser.DEF)


            self.state = 43
            self.match(SysMLv2Parser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 44
                self.match(SysMLv2Parser.COLON)
                self.state = 45
                self.match(SysMLv2Parser.SPECIALIZATION)


            self.state = 48
            self.match(SysMLv2Parser.LBRACE)
            self.state = 49
            self.partBody()
            self.state = 50
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 52
                    self.attributeStmt()
                    pass
                elif token in [5]:
                    self.state = 53
                    self.partStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
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
            self.state = 58
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 59
                self.match(SysMLv2Parser.DEF)


            self.state = 62
            self.match(SysMLv2Parser.ID)
            self.state = 63
            self.match(SysMLv2Parser.COLON)
            self.state = 64
            self.attributeType()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 65
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 66
                self.defaultValue()


            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 69
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.arrayType()
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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 80
                    self.match(SysMLv2Parser.T__1)


                self.state = 83
                self.match(SysMLv2Parser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(SysMLv2Parser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
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
            self.state = 88
            self.match(SysMLv2Parser.LPAREN)
            self.state = 89
            self.defaultValue()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 90
                self.match(SysMLv2Parser.T__2)
                self.state = 91
                self.defaultValue()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
            self.match(SysMLv2Parser.ARRAY)
            self.state = 100
            self.match(SysMLv2Parser.LBRACE)
            self.state = 101
            self.arrayBody()
            self.state = 102
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
            self.state = 104
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 105
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 106
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 107
            self.match(SysMLv2Parser.NUMBER)
            self.state = 108
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 109
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 110
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 111
            self.match(SysMLv2Parser.COLON)
            self.state = 112
            self.attributeType()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 113
                self.match(SysMLv2Parser.LBRACK)
                self.state = 114
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 115
                self.match(SysMLv2Parser.RBRACK)


            self.state = 118
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 119
            self.defaultValue()
            self.state = 120
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






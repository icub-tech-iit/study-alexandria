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
        4,1,27,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,5,0,26,8,0,
        10,0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,3,2,40,8,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,4,3,50,8,3,11,3,12,3,51,1,4,1,4,
        3,4,56,8,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,4,3,4,66,8,4,1,5,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,94,8,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,25,26,106,0,21,1,
        0,0,0,2,32,1,0,0,0,4,37,1,0,0,0,6,49,1,0,0,0,8,53,1,0,0,0,10,72,
        1,0,0,0,12,74,1,0,0,0,14,76,1,0,0,0,16,81,1,0,0,0,18,20,3,2,1,0,
        19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,27,1,
        0,0,0,23,21,1,0,0,0,24,26,3,4,2,0,25,24,1,0,0,0,26,29,1,0,0,0,27,
        25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,
        1,31,1,1,0,0,0,32,33,5,2,0,0,33,34,5,24,0,0,34,35,5,1,0,0,35,36,
        5,8,0,0,36,3,1,0,0,0,37,39,5,3,0,0,38,40,5,6,0,0,39,38,1,0,0,0,39,
        40,1,0,0,0,40,41,1,0,0,0,41,42,5,24,0,0,42,43,5,7,0,0,43,44,5,9,
        0,0,44,45,3,6,3,0,45,46,5,10,0,0,46,5,1,0,0,0,47,50,3,8,4,0,48,50,
        3,4,2,0,49,47,1,0,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,
        51,52,1,0,0,0,52,7,1,0,0,0,53,55,5,4,0,0,54,56,5,6,0,0,55,54,1,0,
        0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,24,0,0,58,59,5,7,0,0,59,
        62,3,10,5,0,60,61,5,5,0,0,61,63,3,12,6,0,62,60,1,0,0,0,62,63,1,0,
        0,0,63,65,1,0,0,0,64,66,5,8,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,9,
        1,0,0,0,67,73,5,16,0,0,68,73,5,17,0,0,69,73,5,18,0,0,70,73,5,19,
        0,0,71,73,3,14,7,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,
        70,1,0,0,0,72,71,1,0,0,0,73,11,1,0,0,0,74,75,7,0,0,0,75,13,1,0,0,
        0,76,77,5,20,0,0,77,78,5,9,0,0,78,79,3,16,8,0,79,80,5,10,0,0,80,
        15,1,0,0,0,81,82,5,21,0,0,82,83,5,22,0,0,83,84,5,5,0,0,84,85,5,25,
        0,0,85,86,5,8,0,0,86,87,5,21,0,0,87,88,5,23,0,0,88,89,5,7,0,0,89,
        93,3,10,5,0,90,91,5,11,0,0,91,92,5,22,0,0,92,94,5,12,0,0,93,90,1,
        0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,5,0,0,96,97,5,13,0,0,97,
        98,3,12,6,0,98,99,5,14,0,0,99,100,1,0,0,0,100,101,5,8,0,0,101,17,
        1,0,0,0,10,21,27,39,49,51,55,62,65,72,93
    ]

class SysMLv2Parser ( Parser ):

    grammarFileName = "SysMLv2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::*'", "'import'", "'part'", "'attribute'", 
                     "'default'", "'def'", "':'", "';'", "'{'", "'}'", "'['", 
                     "']'", "'('", "')'", "'='", "'Integer'", "'String'", 
                     "'Real'", "'Boolean'", "'Array'", "':>>'", "'dimensions'", 
                     "'elements'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IMPORT", "PART", "ATTRIBUTE", 
                      "DEFAULT", "DEF", "COLON", "SEMICOLON", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "LPAREN", "RPAREN", 
                      "EQUALS", "INTEGER", "STRING", "REAL", "BOOLEAN", 
                      "ARRAY", "SPECIALIZE", "DIMENSIONS", "ELEMENTS", "ID", 
                      "NUMBER", "STR", "WS" ]

    RULE_model = 0
    RULE_importStmt = 1
    RULE_partStmt = 2
    RULE_partBody = 3
    RULE_attributeStmt = 4
    RULE_attributeType = 5
    RULE_defaultValue = 6
    RULE_arrayType = 7
    RULE_arrayBody = 8

    ruleNames =  [ "model", "importStmt", "partStmt", "partBody", "attributeStmt", 
                   "attributeType", "defaultValue", "arrayType", "arrayBody" ]

    EOF = Token.EOF
    T__0=1
    IMPORT=2
    PART=3
    ATTRIBUTE=4
    DEFAULT=5
    DEF=6
    COLON=7
    SEMICOLON=8
    LBRACE=9
    RBRACE=10
    LBRACK=11
    RBRACK=12
    LPAREN=13
    RPAREN=14
    EQUALS=15
    INTEGER=16
    STRING=17
    REAL=18
    BOOLEAN=19
    ARRAY=20
    SPECIALIZE=21
    DIMENSIONS=22
    ELEMENTS=23
    ID=24
    NUMBER=25
    STR=26
    WS=27

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 18
                self.importStmt()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 24
                self.partStmt()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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
            self.state = 32
            self.match(SysMLv2Parser.IMPORT)
            self.state = 33
            self.match(SysMLv2Parser.ID)
            self.state = 34
            self.match(SysMLv2Parser.T__0)
            self.state = 35
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

        def COLON(self):
            return self.getToken(SysMLv2Parser.COLON, 0)

        def LBRACE(self):
            return self.getToken(SysMLv2Parser.LBRACE, 0)

        def partBody(self):
            return self.getTypedRuleContext(SysMLv2Parser.PartBodyContext,0)


        def RBRACE(self):
            return self.getToken(SysMLv2Parser.RBRACE, 0)

        def DEF(self):
            return self.getToken(SysMLv2Parser.DEF, 0)

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
            self.state = 37
            self.match(SysMLv2Parser.PART)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 38
                self.match(SysMLv2Parser.DEF)


            self.state = 41
            self.match(SysMLv2Parser.ID)
            self.state = 42
            self.match(SysMLv2Parser.COLON)
            self.state = 43
            self.match(SysMLv2Parser.LBRACE)
            self.state = 44
            self.partBody()
            self.state = 45
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
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 47
                    self.attributeStmt()
                    pass
                elif token in [3]:
                    self.state = 48
                    self.partStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==4):
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
            self.state = 53
            self.match(SysMLv2Parser.ATTRIBUTE)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 54
                self.match(SysMLv2Parser.DEF)


            self.state = 57
            self.match(SysMLv2Parser.ID)
            self.state = 58
            self.match(SysMLv2Parser.COLON)
            self.state = 59
            self.attributeType()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 60
                self.match(SysMLv2Parser.DEFAULT)
                self.state = 61
                self.defaultValue()


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 64
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(SysMLv2Parser.INTEGER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(SysMLv2Parser.STRING)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(SysMLv2Parser.REAL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(SysMLv2Parser.BOOLEAN)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
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
            self.enterOuterAlt(localctx, 1)
            self.state = 74
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
        self.enterRule(localctx, 14, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SysMLv2Parser.ARRAY)
            self.state = 77
            self.match(SysMLv2Parser.LBRACE)
            self.state = 78
            self.arrayBody()
            self.state = 79
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


        def LPAREN(self):
            return self.getToken(SysMLv2Parser.LPAREN, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(SysMLv2Parser.DefaultValueContext,0)


        def RPAREN(self):
            return self.getToken(SysMLv2Parser.RPAREN, 0)

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
        self.enterRule(localctx, 16, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 82
            self.match(SysMLv2Parser.DIMENSIONS)
            self.state = 83
            self.match(SysMLv2Parser.DEFAULT)
            self.state = 84
            self.match(SysMLv2Parser.NUMBER)
            self.state = 85
            self.match(SysMLv2Parser.SEMICOLON)
            self.state = 86
            self.match(SysMLv2Parser.SPECIALIZE)
            self.state = 87
            self.match(SysMLv2Parser.ELEMENTS)
            self.state = 88
            self.match(SysMLv2Parser.COLON)
            self.state = 89
            self.attributeType()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 90
                self.match(SysMLv2Parser.LBRACK)
                self.state = 91
                self.match(SysMLv2Parser.DIMENSIONS)
                self.state = 92
                self.match(SysMLv2Parser.RBRACK)


            self.state = 95
            self.match(SysMLv2Parser.DEFAULT)

            self.state = 96
            self.match(SysMLv2Parser.LPAREN)
            self.state = 97
            self.defaultValue()
            self.state = 98
            self.match(SysMLv2Parser.RPAREN)
            self.state = 100
            self.match(SysMLv2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






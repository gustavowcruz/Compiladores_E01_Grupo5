# Generated from RoboLang.g4 by ANTLR 4.13.2
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
        4,1,16,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,3,6,56,8,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,0,0,11,
        0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,8,9,66,0,22,1,0,0,0,2,32,1,0,
        0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,46,1,0,0,0,10,49,1,0,0,0,12,52,1,
        0,0,0,14,57,1,0,0,0,16,63,1,0,0,0,18,66,1,0,0,0,20,69,1,0,0,0,22,
        23,5,1,0,0,23,24,5,14,0,0,24,25,5,12,0,0,25,26,3,2,1,0,26,27,5,13,
        0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,31,3,4,2,0,30,29,1,0,0,0,31,34,
        1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,1,0,0,0,34,32,1,0,0,0,35,
        41,3,6,3,0,36,41,3,8,4,0,37,41,3,10,5,0,38,41,3,12,6,0,39,41,3,14,
        7,0,40,35,1,0,0,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,
        1,0,0,0,41,5,1,0,0,0,42,43,5,2,0,0,43,44,5,11,0,0,44,45,3,16,8,0,
        45,7,1,0,0,0,46,47,5,3,0,0,47,48,3,18,9,0,48,9,1,0,0,0,49,50,5,4,
        0,0,50,51,5,15,0,0,51,11,1,0,0,0,52,53,5,5,0,0,53,55,5,15,0,0,54,
        56,5,10,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,13,1,0,0,0,57,58,5,6,
        0,0,58,59,5,15,0,0,59,60,5,12,0,0,60,61,3,2,1,0,61,62,5,13,0,0,62,
        15,1,0,0,0,63,64,5,15,0,0,64,65,3,20,10,0,65,17,1,0,0,0,66,67,5,
        15,0,0,67,68,5,7,0,0,68,19,1,0,0,0,69,70,7,0,0,0,70,21,1,0,0,0,3,
        32,40,55
    ]

class RoboLangParser ( Parser ):

    grammarFileName = "RoboLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'robo'", "'mover'", "'virar'", "'velocidade'", 
                     "'esperar'", "'repetir'", "'graus'", "'cm'", "'m'", 
                     "'ms'", "<INVALID>", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ROBO", "MOVER", "VIRAR", "VELOCIDADE", 
                      "ESPERAR", "REPETIR", "GRAUS", "CM", "M", "MS", "EIXO", 
                      "LBRACE", "RBRACE", "ID", "NUMBER", "WS" ]

    RULE_programa = 0
    RULE_listaComandos = 1
    RULE_comando = 2
    RULE_mover = 3
    RULE_virar = 4
    RULE_velocidade = 5
    RULE_esperar = 6
    RULE_repetir = 7
    RULE_distancia = 8
    RULE_angulo = 9
    RULE_unidade = 10

    ruleNames =  [ "programa", "listaComandos", "comando", "mover", "virar", 
                   "velocidade", "esperar", "repetir", "distancia", "angulo", 
                   "unidade" ]

    EOF = Token.EOF
    ROBO=1
    MOVER=2
    VIRAR=3
    VELOCIDADE=4
    ESPERAR=5
    REPETIR=6
    GRAUS=7
    CM=8
    M=9
    MS=10
    EIXO=11
    LBRACE=12
    RBRACE=13
    ID=14
    NUMBER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROBO(self):
            return self.getToken(RoboLangParser.ROBO, 0)

        def ID(self):
            return self.getToken(RoboLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(RoboLangParser.LBRACE, 0)

        def listaComandos(self):
            return self.getTypedRuleContext(RoboLangParser.ListaComandosContext,0)


        def RBRACE(self):
            return self.getToken(RoboLangParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(RoboLangParser.EOF, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = RoboLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(RoboLangParser.ROBO)
            self.state = 23
            self.match(RoboLangParser.ID)
            self.state = 24
            self.match(RoboLangParser.LBRACE)
            self.state = 25
            self.listaComandos()
            self.state = 26
            self.match(RoboLangParser.RBRACE)
            self.state = 27
            self.match(RoboLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RoboLangParser.ComandoContext)
            else:
                return self.getTypedRuleContext(RoboLangParser.ComandoContext,i)


        def getRuleIndex(self):
            return RoboLangParser.RULE_listaComandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaComandos" ):
                listener.enterListaComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaComandos" ):
                listener.exitListaComandos(self)




    def listaComandos(self):

        localctx = RoboLangParser.ListaComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_listaComandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0):
                self.state = 29
                self.comando()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mover(self):
            return self.getTypedRuleContext(RoboLangParser.MoverContext,0)


        def virar(self):
            return self.getTypedRuleContext(RoboLangParser.VirarContext,0)


        def velocidade(self):
            return self.getTypedRuleContext(RoboLangParser.VelocidadeContext,0)


        def esperar(self):
            return self.getTypedRuleContext(RoboLangParser.EsperarContext,0)


        def repetir(self):
            return self.getTypedRuleContext(RoboLangParser.RepetirContext,0)


        def getRuleIndex(self):
            return RoboLangParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = RoboLangParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comando)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.mover()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.virar()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.velocidade()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.esperar()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.repetir()
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


    class MoverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVER(self):
            return self.getToken(RoboLangParser.MOVER, 0)

        def EIXO(self):
            return self.getToken(RoboLangParser.EIXO, 0)

        def distancia(self):
            return self.getTypedRuleContext(RoboLangParser.DistanciaContext,0)


        def getRuleIndex(self):
            return RoboLangParser.RULE_mover

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMover" ):
                listener.enterMover(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMover" ):
                listener.exitMover(self)




    def mover(self):

        localctx = RoboLangParser.MoverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mover)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(RoboLangParser.MOVER)
            self.state = 43
            self.match(RoboLangParser.EIXO)
            self.state = 44
            self.distancia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VirarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIRAR(self):
            return self.getToken(RoboLangParser.VIRAR, 0)

        def angulo(self):
            return self.getTypedRuleContext(RoboLangParser.AnguloContext,0)


        def getRuleIndex(self):
            return RoboLangParser.RULE_virar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVirar" ):
                listener.enterVirar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVirar" ):
                listener.exitVirar(self)




    def virar(self):

        localctx = RoboLangParser.VirarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_virar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(RoboLangParser.VIRAR)
            self.state = 47
            self.angulo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VelocidadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VELOCIDADE(self):
            return self.getToken(RoboLangParser.VELOCIDADE, 0)

        def NUMBER(self):
            return self.getToken(RoboLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_velocidade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVelocidade" ):
                listener.enterVelocidade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVelocidade" ):
                listener.exitVelocidade(self)




    def velocidade(self):

        localctx = RoboLangParser.VelocidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_velocidade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(RoboLangParser.VELOCIDADE)
            self.state = 50
            self.match(RoboLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EsperarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESPERAR(self):
            return self.getToken(RoboLangParser.ESPERAR, 0)

        def NUMBER(self):
            return self.getToken(RoboLangParser.NUMBER, 0)

        def MS(self):
            return self.getToken(RoboLangParser.MS, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_esperar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsperar" ):
                listener.enterEsperar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsperar" ):
                listener.exitEsperar(self)




    def esperar(self):

        localctx = RoboLangParser.EsperarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_esperar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(RoboLangParser.ESPERAR)
            self.state = 53
            self.match(RoboLangParser.NUMBER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 54
                self.match(RoboLangParser.MS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPETIR(self):
            return self.getToken(RoboLangParser.REPETIR, 0)

        def NUMBER(self):
            return self.getToken(RoboLangParser.NUMBER, 0)

        def LBRACE(self):
            return self.getToken(RoboLangParser.LBRACE, 0)

        def listaComandos(self):
            return self.getTypedRuleContext(RoboLangParser.ListaComandosContext,0)


        def RBRACE(self):
            return self.getToken(RoboLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_repetir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetir" ):
                listener.enterRepetir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetir" ):
                listener.exitRepetir(self)




    def repetir(self):

        localctx = RoboLangParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_repetir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(RoboLangParser.REPETIR)
            self.state = 58
            self.match(RoboLangParser.NUMBER)
            self.state = 59
            self.match(RoboLangParser.LBRACE)
            self.state = 60
            self.listaComandos()
            self.state = 61
            self.match(RoboLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DistanciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RoboLangParser.NUMBER, 0)

        def unidade(self):
            return self.getTypedRuleContext(RoboLangParser.UnidadeContext,0)


        def getRuleIndex(self):
            return RoboLangParser.RULE_distancia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistancia" ):
                listener.enterDistancia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistancia" ):
                listener.exitDistancia(self)




    def distancia(self):

        localctx = RoboLangParser.DistanciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_distancia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RoboLangParser.NUMBER)
            self.state = 64
            self.unidade()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnguloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RoboLangParser.NUMBER, 0)

        def GRAUS(self):
            return self.getToken(RoboLangParser.GRAUS, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_angulo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngulo" ):
                listener.enterAngulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngulo" ):
                listener.exitAngulo(self)




    def angulo(self):

        localctx = RoboLangParser.AnguloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_angulo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(RoboLangParser.NUMBER)
            self.state = 67
            self.match(RoboLangParser.GRAUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnidadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(RoboLangParser.CM, 0)

        def M(self):
            return self.getToken(RoboLangParser.M, 0)

        def getRuleIndex(self):
            return RoboLangParser.RULE_unidade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnidade" ):
                listener.enterUnidade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnidade" ):
                listener.exitUnidade(self)




    def unidade(self):

        localctx = RoboLangParser.UnidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unidade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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






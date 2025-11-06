# Generated from RoboLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RoboLangParser import RoboLangParser
else:
    from RoboLangParser import RoboLangParser

# This class defines a complete listener for a parse tree produced by RoboLangParser.
class RoboLangListener(ParseTreeListener):

    # Enter a parse tree produced by RoboLangParser#programa.
    def enterPrograma(self, ctx:RoboLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by RoboLangParser#programa.
    def exitPrograma(self, ctx:RoboLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by RoboLangParser#listaComandos.
    def enterListaComandos(self, ctx:RoboLangParser.ListaComandosContext):
        pass

    # Exit a parse tree produced by RoboLangParser#listaComandos.
    def exitListaComandos(self, ctx:RoboLangParser.ListaComandosContext):
        pass


    # Enter a parse tree produced by RoboLangParser#comando.
    def enterComando(self, ctx:RoboLangParser.ComandoContext):
        pass

    # Exit a parse tree produced by RoboLangParser#comando.
    def exitComando(self, ctx:RoboLangParser.ComandoContext):
        pass


    # Enter a parse tree produced by RoboLangParser#mover.
    def enterMover(self, ctx:RoboLangParser.MoverContext):
        pass

    # Exit a parse tree produced by RoboLangParser#mover.
    def exitMover(self, ctx:RoboLangParser.MoverContext):
        pass


    # Enter a parse tree produced by RoboLangParser#virar.
    def enterVirar(self, ctx:RoboLangParser.VirarContext):
        pass

    # Exit a parse tree produced by RoboLangParser#virar.
    def exitVirar(self, ctx:RoboLangParser.VirarContext):
        pass


    # Enter a parse tree produced by RoboLangParser#velocidade.
    def enterVelocidade(self, ctx:RoboLangParser.VelocidadeContext):
        pass

    # Exit a parse tree produced by RoboLangParser#velocidade.
    def exitVelocidade(self, ctx:RoboLangParser.VelocidadeContext):
        pass


    # Enter a parse tree produced by RoboLangParser#esperar.
    def enterEsperar(self, ctx:RoboLangParser.EsperarContext):
        pass

    # Exit a parse tree produced by RoboLangParser#esperar.
    def exitEsperar(self, ctx:RoboLangParser.EsperarContext):
        pass


    # Enter a parse tree produced by RoboLangParser#repetir.
    def enterRepetir(self, ctx:RoboLangParser.RepetirContext):
        pass

    # Exit a parse tree produced by RoboLangParser#repetir.
    def exitRepetir(self, ctx:RoboLangParser.RepetirContext):
        pass


    # Enter a parse tree produced by RoboLangParser#distancia.
    def enterDistancia(self, ctx:RoboLangParser.DistanciaContext):
        pass

    # Exit a parse tree produced by RoboLangParser#distancia.
    def exitDistancia(self, ctx:RoboLangParser.DistanciaContext):
        pass


    # Enter a parse tree produced by RoboLangParser#angulo.
    def enterAngulo(self, ctx:RoboLangParser.AnguloContext):
        pass

    # Exit a parse tree produced by RoboLangParser#angulo.
    def exitAngulo(self, ctx:RoboLangParser.AnguloContext):
        pass


    # Enter a parse tree produced by RoboLangParser#unidade.
    def enterUnidade(self, ctx:RoboLangParser.UnidadeContext):
        pass

    # Exit a parse tree produced by RoboLangParser#unidade.
    def exitUnidade(self, ctx:RoboLangParser.UnidadeContext):
        pass



del RoboLangParser
# Generated from RoboLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RoboLangParser import RoboLangParser
else:
    from RoboLangParser import RoboLangParser

# This class defines a complete generic visitor for a parse tree produced by RoboLangParser.

class RoboLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RoboLangParser#programa.
    def visitPrograma(self, ctx:RoboLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#listaComandos.
    def visitListaComandos(self, ctx:RoboLangParser.ListaComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#comando.
    def visitComando(self, ctx:RoboLangParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#mover.
    def visitMover(self, ctx:RoboLangParser.MoverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#virar.
    def visitVirar(self, ctx:RoboLangParser.VirarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#velocidade.
    def visitVelocidade(self, ctx:RoboLangParser.VelocidadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#esperar.
    def visitEsperar(self, ctx:RoboLangParser.EsperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#repetir.
    def visitRepetir(self, ctx:RoboLangParser.RepetirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#distancia.
    def visitDistancia(self, ctx:RoboLangParser.DistanciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#angulo.
    def visitAngulo(self, ctx:RoboLangParser.AnguloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RoboLangParser#unidade.
    def visitUnidade(self, ctx:RoboLangParser.UnidadeContext):
        return self.visitChildren(ctx)



del RoboLangParser
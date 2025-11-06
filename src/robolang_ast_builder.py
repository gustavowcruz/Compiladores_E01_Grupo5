"""
Visitor that builds the AST from the ANTLR parse tree.

Usage notes:
- Generate the Python parser/lexer/visitor with ANTLR first, e.g.:
  java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 RoboLang.g4
- Install runtime: pip install antlr4-python3-runtime
- Then run code that parses an input and calls ASTBuilder().visit(tree)
"""
from typing import List

try:
    from src.RoboLangParser import RoboLangParser
    from src.RoboLangVisitor import RoboLangVisitor
except Exception:
    # If the generated files are not present yet this import will fail.
    # The user must run ANTLR to generate the Python runtime files from RoboLang.g4
    RoboLangParser = None
    RoboLangVisitor = object

from .ast import Program, Move, Turn, Speed, Wait, Repeat, Distance, Angle


class ASTBuilder(RoboLangVisitor):
    """Builds the AST by visiting parse-tree nodes."""

    # program: ROBO ID LBRACE listaComandos RBRACE EOF;
    def visitPrograma(self, ctx):
        name = ctx.ID().getText()
        lista = self.visit(ctx.listaComandos())
        return Program(name=name, commands=lista)

    # listaComandos: comando* ;
    def visitListaComandos(self, ctx):
        commands = []
        for c in ctx.comando():
            commands.append(self.visit(c))
        return commands

    # comando: mover | virar | velocidade | esperar | repetir ;
    def visitComando(self, ctx):
        # The rule has alternatives; delegate to the child-specific visit
        # Each alternative is a single child node
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            # if it's a rule node, visit it
            try:
                # ctx.getChild(i) may be a TerminalNode; skip if visitor won't handle
                res = self.visit(child)
                if res is not None:
                    return res
            except Exception:
                continue
        return None

    # mover: MOVER EIXO distancia ;
    def visitMover(self, ctx):
        axis = ctx.EIXO().getText()
        dist = self.visit(ctx.distancia())
        return Move(axis=axis, distance=dist.value, unit=dist.unit)

    # virar: VIRAR angulo ;
    def visitVirar(self, ctx):
        ang = self.visit(ctx.angulo())
        return Turn(degrees=ang.value)

    # velocidade: VELOCIDADE NUMBER ;
    def visitVelocidade(self, ctx):
        num = float(ctx.NUMBER().getText())
        return Speed(value=num)

    # esperar: ESPERAR NUMBER MS? ;
    def visitEsperar(self, ctx):
        num = float(ctx.NUMBER().getText())
        ms = ctx.MS() is not None
        return Wait(duration=num, ms=ms)

    # repetir: REPETIR NUMBER LBRACE listaComandos RBRACE ;
    def visitRepetir(self, ctx):
        count = int(float(ctx.NUMBER().getText()))
        body = self.visit(ctx.listaComandos())
        return Repeat(count=count, commands=body)

    # distancia: NUMBER unidade ;
    def visitDistancia(self, ctx):
        val = float(ctx.NUMBER().getText())
        unit = self.visit(ctx.unidade())
        return Distance(value=val, unit=unit)

    # angulo: NUMBER GRAUS ;
    def visitAngulo(self, ctx):
        val = float(ctx.NUMBER().getText())
        return Angle(value=val)

    # unidade: CM | M ;
    def visitUnidade(self, ctx):
        # unidade has a terminal directly
        if ctx.CM() is not None:
            return ctx.CM().getText()
        if ctx.M() is not None:
            return ctx.M().getText()
        return ''

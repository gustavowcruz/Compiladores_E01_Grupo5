from antlr4 import FileStream, CommonTokenStream
from RoboLangLexer import RoboLangLexer
from RoboLangParser import RoboLangParser
from src.robolang_ast_builder import ASTBuilder


def main():
    input_stream = FileStream('example.robo', encoding='utf-8')
    lexer = RoboLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = RoboLangParser(tokens)
    tree = parser.programa()
    builder = ASTBuilder()
    ast = builder.visit(tree)
    print(ast)


if __name__ == '__main__':
    main()

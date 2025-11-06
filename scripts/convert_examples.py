import json
from pathlib import Path

from antlr4 import FileStream, CommonTokenStream
from RoboLangLexer import RoboLangLexer
from RoboLangParser import RoboLangParser
from src.robolang_ast_builder import ASTBuilder
from src.ast_utils import ast_to_dict


EXAMPLES_DIR = Path(__file__).resolve().parent.parent / 'examples'


def convert_file(path: Path):
    src = path.read_text(encoding='utf-8')
    input_stream = FileStream(str(path), encoding='utf-8')
    lexer = RoboLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = RoboLangParser(tokens)
    tree = parser.programa()
    builder = ASTBuilder()
    ast = builder.visit(tree)
    return src, ast


def main():
    print('Converting examples in', EXAMPLES_DIR)
    for f in sorted(EXAMPLES_DIR.glob('*.robo')):
        print('\n---')
        print('File:', f.name)
        src, ast = convert_file(f)
        print('Source:')
        print(src)
        d = ast_to_dict(ast)
        print('AST (JSON):')
        print(json.dumps(d, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

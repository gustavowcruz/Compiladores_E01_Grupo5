from antlr4 import *
from RoboLangLexer import RoboLangLexer
from RoboLangParser import RoboLangParser
from RoboLangListener import RoboLangListener
# Exemplo de código RoboLang para parsear
input_text = """
robo meuRobo {
    velocidade 100
    mover x 50 cm
    virar 90 graus
    mover y 30 cm
    esperar 1000 ms
    repetir 3 {
        mover z 10 cm
        virar 45 graus
    }
}
"""
def main():
    # Criar o input stream
    input_stream = InputStream(input_text)
    
    # Criar o lexer
    lexer = RoboLangLexer(input_stream)
    
    # Criar o token stream
    token_stream = CommonTokenStream(lexer)
    
    # Criar o parser
    parser = RoboLangParser(token_stream)
    
    # Parsear o programa
    tree = parser.programa()
    
    # Imprimir a árvore
    print("Parse tree:")
    print(tree.toStringTree(recog=parser))
    print("\n✓ Programa RoboLang parseado com sucesso!")

if __name__ == '__main__':
    main()

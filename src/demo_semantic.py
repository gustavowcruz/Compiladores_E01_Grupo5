"""
Demonstrate semantic analysis with specific examples.
Shows both valid and invalid programs.
"""
from pathlib import Path
from antlr4 import FileStream, CommonTokenStream
from src.RoboLangLexer import RoboLangLexer
from src.RoboLangParser import RoboLangParser
from src.robolang_ast_builder import ASTBuilder
from src.semantic_analyzer import SemanticAnalyzer


def analyze_example(name: str, code: str):
    """Parse and analyze a code snippet."""
    print(f"\n{'='*70}")
    print(f"Exêmplo: {name}")
    print('='*70)
    print("Código:")
    print(code)
    print()
    
    # Save to temp file and parse
    temp_file = Path('temp_example.robo')
    temp_file.write_text(code, encoding='utf-8')
    
    try:
        input_stream = FileStream(str(temp_file), encoding='utf-8')
        lexer = RoboLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = RoboLangParser(tokens)
        tree = parser.programa()
        
        # Build AST
        builder = ASTBuilder()
        ast = builder.visit(tree)
        
        # Semantic analysis
        analyzer = SemanticAnalyzer(collect_all_errors=True)
        is_valid = analyzer.analyze(ast)
        
        print(f"Programa: {ast.name}")
        
        if is_valid:
            print("✅ SEMANTICAMENTE VÁLIDO")
        else:
            print("❌ ERROS SEMANTICOS ENCONTRADOS:")
            for i, error in enumerate(analyzer.get_errors(), 1):
                print(f"  {i}. {error}")
    
    finally:
        if temp_file.exists():
            temp_file.unlink()
    
    return is_valid


def main():
    print("="*70)
    print("DEMONSTRAÇÃO DO ANÁLISE SEMÂNTICA")
    print("="*70)
    
    # Valid examples
    print("\n" + "▸"*35)
    print("PROGRAMAS VÁLIDOS")
    print("▸"*35)
    
    analyze_example(
        "Programa simples válido",
        """robo simples {
  mover x 15 cm
  virar 180 graus
  velocidade 5
}"""
    )
    
    analyze_example(
        "Programa com repetição",
        """robo repetidor {
  repetir 3 {
    mover y 55 m
    esperar 100 ms
  }
}"""
    )
    
    print("\n\n" + "▸"*35)
    print("PROGRAMAS INVÁLIDOS")
    print("▸"*35)

    analyze_example(
        "Ângulo válido (< 0)",
        """robo valido {
  virar 90 graus
  esperar 50 ms
  velocidade 5
}"""
    )

    analyze_example(
        "Ângulo Inválido (> 360)",
        """robo invalido {
  virar 400 graus
}"""
    )
    
    analyze_example(
        "Distância zero",
        """robo invalido {
  mover x 0 cm
}"""
    )
    
    analyze_example(
        "Velocidade zero",
        """robo invalido {
  velocidade 0
}"""
    )
    
    analyze_example(
        "Espera zero",
        """robo invalido {
  esperar 0 ms
}"""
    )
    
    analyze_example(
        "Contagem de repetição inválida",
        """robo invalido {
  repetir 0 {
    mover x 5 cm
  }
}"""
    )
    
    analyze_example(
        "Erros múltiplos",
        """robo multi_erro {
  mover x 0 cm
  virar 400 graus
  velocidade 0
  esperar 0 ms
}"""
    )
    
    print("\n" + "="*70)
    print("DEMOSTRAÇÃO FINALIZADA")
    print("="*70)


if __name__ == '__main__':
    main()

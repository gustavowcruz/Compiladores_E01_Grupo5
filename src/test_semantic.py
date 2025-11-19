"""
Test semantic analyzer with valid and invalid examples.
"""
import json
from pathlib import Path

from antlr4 import FileStream, CommonTokenStream
from src.RoboLangLexer import RoboLangLexer
from src.RoboLangParser import RoboLangParser
from src.robolang_ast_builder import ASTBuilder
from src.semantic_analyzer import SemanticAnalyzer
from src.semantic_errors import SemanticError


def analyze_file(path: Path):
    """Parse and analyze a RoboLang file."""
    print(f"\n{'='*60}")
    print(f"Analisando: {path.name}")
    print('='*60)
    
    # Parse
    input_stream = FileStream(str(path), encoding='utf-8')
    lexer = RoboLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = RoboLangParser(tokens)
    tree = parser.programa()
    
    # Build AST
    builder = ASTBuilder()
    ast = builder.visit(tree)
    
    print(f"\nProgram: {ast.name}")
    print(f"Commands: {len(ast.commands)}")
    
    # Semantic analysis
    analyzer = SemanticAnalyzer(collect_all_errors=True)
    is_valid = analyzer.analyze(ast)
    
    if is_valid:
        print("\n✅ VÁLIDO - Sem erros semânticos encontrados")
    else:
        print("\n❌ INVÁLIDO - Erros semânticos encontrados:")
        for error in analyzer.get_errors():
            print(f"  • {error}")
    
    return is_valid, analyzer.get_errors()


def create_invalid_examples():
    examples = [
        ("distancia_negativa.robo", """robo test {
  mover x -10 cm
}"""),
        ("angulo_invalido.robo", """robo test {
  virar 400 graus
}"""),
        ("velocidade_invalida.robo", """robo test {
  velocidade -5
}"""),
        ("espera_invalida.robo", """robo test {
  esperar -100 ms
}"""),
        ("repetir_invalido.robo", """robo test {
  repetir 0 {
    mover x 5 cm
  }
}"""),
    ]
    
    test_dir = Path(__file__).resolve().parent.parent / 'exemplos' / 'invalidos'
    test_dir.mkdir(exist_ok=True)
    
    created_files = []
    for filename, content in examples:
        file_path = test_dir / filename
        file_path.write_text(content, encoding='utf-8')
        created_files.append(file_path)
    
    return created_files


def main():
    print("TESTE DE ANÁLISE SEMÂNTICA")
    print("="*60)
    
    exemplos_dir = Path(__file__).resolve().parent.parent / 'exemplos'
    invalidos_dir = exemplos_dir / 'invalidos'
    
    # Test valid examples
    print("\n\n>>> TESTANDO EXEMPLOS VÁLIDOS <<<")
    valid_count = 0
    for f in sorted(exemplos_dir.glob('exemplo*.robo')):
        is_valid, _ = analyze_file(f)
        if is_valid:
            valid_count += 1
    
    # Test invalid examples from invalidos/ folder
    print("\n\n>>> TESTANDO EXEMPLOS INVÁLIDOS (pasta invalidos/) <<<")
    invalid_count = 0
    total_invalid = 0
    if invalidos_dir.exists():
        invalid_files = sorted(invalidos_dir.glob('*.robo'))
        total_invalid = len(invalid_files)
        for f in invalid_files:
            is_valid, _ = analyze_file(f)
            if not is_valid:
                invalid_count += 1
    
    # Create additional invalid examples for testing
    print("\n\n>>> CRIANDO E TESTANDO EXEMPLOS INVÁLIDOS ADICIONAIS <<<")
    created_files = create_invalid_examples()
    created_invalid_count = 0
    for f in created_files:
        is_valid, _ = analyze_file(f)
        if not is_valid:
            created_invalid_count += 1
    
    # Resumo
    print("\n\n" + "="*60)
    print("RESUMO:")
    print("="*60)
    print(f"Exemplos válidos aprovados: {valid_count}")
    print(f"Exemplos inválidos detectados (pasta invalidos/): {invalid_count}/{total_invalid}")
    print(f"Exemplos inválidos criados e detectados: {created_invalid_count}/{len(created_files)}")
    print(f"Total de inválidos detectados: {invalid_count + created_invalid_count}/{total_invalid + len(created_files)}")
    print("="*60)


if __name__ == '__main__':
    main()

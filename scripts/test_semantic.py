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
    print(f"Analyzing: {path.name}")
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
        print("\n✅ VALID - No semantic errors found")
    else:
        print("\n❌ INVALID - Semantic errors found:")
        for error in analyzer.get_errors():
            print(f"  • {error}")
    
    return is_valid, analyzer.get_errors()


def create_invalid_examples():
    """Create some invalid examples for testing."""
    examples = [
        ("invalid_negative_distance.robo", """robo test {
  mover x -10 cm
}"""),
        ("invalid_angle.robo", """robo test {
  virar 400 graus
}"""),
        ("invalid_speed.robo", """robo test {
  velocidade -5
}"""),
        ("invalid_wait.robo", """robo test {
  esperar -100 ms
}"""),
        ("invalid_repeat.robo", """robo test {
  repetir 0 {
    mover x 5 cm
  }
}"""),
    ]
    
    test_dir = Path(__file__).resolve().parent.parent / 'exemplos' / 'invalid'
    test_dir.mkdir(exist_ok=True)
    
    created_files = []
    for filename, content in examples:
        file_path = test_dir / filename
        file_path.write_text(content, encoding='utf-8')
        created_files.append(file_path)
    
    return created_files


def main():
    print("SEMANTIC ANALYZER TEST")
    print("="*60)
    
    exemplos_dir = Path(__file__).resolve().parent.parent / 'exemplos'
    
    # Test valid examples
    print("\n\n>>> TESTING VALID EXAMPLES <<<")
    valid_count = 0
    for f in sorted(exemplos_dir.glob('exemplo*.robo')):
        is_valid, _ = analyze_file(f)
        if is_valid:
            valid_count += 1
    
    # Create and test invalid examples
    print("\n\n>>> TESTING INVALID EXAMPLES <<<")
    invalid_files = create_invalid_examples()
    invalid_count = 0
    for f in invalid_files:
        is_valid, _ = analyze_file(f)
        if not is_valid:
            invalid_count += 1
    
    # Summary
    print("\n\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Valid examples passed: {valid_count}")
    print(f"Invalid examples detected: {invalid_count}/{len(invalid_files)}")
    print("="*60)


if __name__ == '__main__':
    main()

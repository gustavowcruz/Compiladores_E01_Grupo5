# Manual de Uso - RoboLang Compiler

Este manual ensina como usar o compilador RoboLang, adicionar novos exemplos e executar as análises sintática e semântica.

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Como Executar os Exemplos](#como-executar-os-exemplos)
4. [Como Adicionar Novos Exemplos](#como-adicionar-novos-exemplos)
5. [Comandos Disponíveis](#comandos-disponíveis)
6. [Estrutura da Linguagem RoboLang](#estrutura-da-linguagem-robolang)
7. [Regras Semânticas](#regras-semânticas)
8. [Troubleshooting](#troubleshooting)

---

## 🔍 Visão Geral

O compilador RoboLang realiza:
- **Análise Léxica e Sintática** (via ANTLR)
- **Construção de AST** (Abstract Syntax Tree)
- **Análise Semântica** (validação de valores e tipos)
- **Conversão para JSON** (representação intermediária)

---

## 📁 Estrutura do Projeto

```
Compiladores_E01_Grupo5/
├── src/
│   ├── RoboLangLexer.py          # Gerado pelo ANTLR
│   ├── RoboLangParser.py         # Gerado pelo ANTLR
│   ├── RoboLangVisitor.py        # Gerado pelo ANTLR
│   ├── ast.py                    # Definição dos nós da AST
│   ├── robolang_ast_builder.py   # Construtor da AST
│   ├── semantic_analyzer.py      # Analisador semântico
│   ├── semantic_errors.py        # Classes de erros
│   ├── ast_utils.py              # Utilitários (conversão JSON)
│   ├── convert_examples.py       # Converte exemplos para JSON
│   ├── demo_semantic.py          # Demonstração do analisador
│   └── test_semantic.py          # Testes automáticos
├── exemplos/
│   ├── exemplo1.robo             # Exemplo válido 1
│   ├── exemplo2.robo             # Exemplo válido 2
│   ├── exemplo3.robo             # Exemplo válido 3
│   └── invalid/                  # Exemplos inválidos
│       ├── invalid_angle.robo
│       ├── invalid_repeat.robo
│       └── ...
├── RoboLang.g4                   # Gramática ANTLR
├── requirements.txt              # Dependências Python
└── antlr-4.13.1-complete.jar     # JAR do ANTLR
```

---

## ▶️ Como Executar os Exemplos

### 1. Demonstração do Analisador Semântico

```powershell
cd C:\Users\gwgus\Documents\Compiladores_E01_Grupo5
python -m src.demo_semantic
```

**Saída:**
- Exemplos válidos aprovados ✅
- Exemplos inválidos com erros detectados ❌
- Descrição clara de cada erro semântico

### 2. Converter Exemplos para AST (JSON)

```powershell
python -m src.convert_examples
```

**Saída:**
- Código-fonte de cada arquivo `.robo` em `exemplos/`
- AST correspondente em formato JSON

### 3. Testar Todos os Exemplos

```powershell
python -m src.test_semantic
```

**Saída:**
- Resumo de exemplos válidos aprovados
- Resumo de exemplos inválidos detectados

---

## ➕ Como Adicionar Novos Exemplos

### Exemplos Válidos

1. **Crie um arquivo `.robo` em `exemplos/`**

```powershell
# Exemplo: criar exemplo4.robo
cd exemplos
notepad exemplo4.robo
```

2. **Escreva o código RoboLang:**

```
robo meuRobo {
  velocidade 10
  mover x 50 cm
  virar 180 graus
  esperar 500 ms
  repetir 5 {
    mover y 10 m
    virar 45 graus
  }
}
```

3. **Execute para validar:**

```powershell
python -m src.convert_examples
```

### Exemplos Inválidos (para testes)

1. **Crie um arquivo `.robo` em `exemplos/invalid/`**

```powershell
cd exemplos\invalid
notepad teste_invalido.robo
```

2. **Escreva código com erros intencionais:**

```
robo teste {
  virar 500 graus
  velocidade 0
}
```

3. **Execute para verificar detecção de erros:**

```powershell
python -m src.test_semantic
```

**Erros esperados:**
- Ângulo 500° (deve ser 0-360)
- Velocidade 0 (deve ser > 0)

---

## 🎮 Comandos Disponíveis

### Gerar Arquivos ANTLR (se modificar a gramática)

```powershell
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o src RoboLang.g4
```

### Instalar Dependências

```powershell
pip install -r requirements.txt
```

### Executar Script Específico

```powershell
# Demonstração semântica
python -m src.demo_semantic

# Conversão de exemplos
python -m src.convert_examples

# Testes completos
python -m src.test_semantic
```

---

## 📝 Estrutura da Linguagem RoboLang

### Sintaxe Geral

```
robo <nome> {
  <comandos>
}
```

### Comandos Disponíveis

#### 1. **Mover**
```
mover <eixo> <distancia> <unidade>
```
- **Eixo:** `x`, `y` ou `z`
- **Distância:** número positivo
- **Unidade:** `cm` ou `m`

**Exemplos:**
```
mover x 10 cm
mover y 5.5 m
mover z 100 cm
```

#### 2. **Virar**
```
virar <angulo> graus
```
- **Ângulo:** 0 a 360

**Exemplos:**
```
virar 90 graus
virar 180 graus
virar 45.5 graus
```

#### 3. **Velocidade**
```
velocidade <valor>
```
- **Valor:** número positivo

**Exemplos:**
```
velocidade 5
velocidade 10.5
```

#### 4. **Esperar**
```
esperar <duracao> [ms]
```
- **Duração:** número positivo
- **ms:** opcional (milissegundos)

**Exemplos:**
```
esperar 100 ms
esperar 2
```

#### 5. **Repetir**
```
repetir <count> {
  <comandos>
}
```
- **Count:** número inteiro >= 1
- **Comandos:** qualquer comando válido (pode aninhar)

**Exemplos:**
```
repetir 3 {
  mover x 5 cm
  virar 90 graus
}

repetir 2 {
  velocidade 10
  repetir 5 {
    mover y 1 m
  }
}
```

### Exemplo Completo

```
robo explorador {
  velocidade 8
  mover x 100 cm
  virar 90 graus
  esperar 500 ms
  
  repetir 4 {
    mover y 50 cm
    virar 90 graus
    esperar 200 ms
  }
  
  mover z 20 m
}
```

---

## ✅ Regras Semânticas

O analisador semântico valida:

### 1. Valores Numéricos
- ✅ **Distâncias:** devem ser > 0
- ✅ **Velocidades:** devem ser > 0
- ✅ **Durações de espera:** devem ser > 0
- ✅ **Ângulos:** devem estar entre 0 e 360 graus
- ✅ **Contador de repetição:** deve ser >= 1

### 2. Unidades
- ✅ **Distância:** apenas `cm` ou `m`
- ✅ **Eixos:** apenas `x`, `y` ou `z`

### 3. Nome do Programa
- ✅ Não pode ser vazio

### Exemplos de Erros

```
robo invalido {
  mover x 0 cm          # ❌ Distância zero
  virar 400 graus       # ❌ Ângulo > 360
  velocidade 0          # ❌ Velocidade zero
  esperar 0 ms          # ❌ Duração zero
  repetir 0 {           # ❌ Contador < 1
    mover y 5 m
  }
}
```

**Saída esperada:**
```
❌ ERROS SEMÂNTICOS ENCONTRADOS:
  1. Move distance must be positive, got 0.0
  2. Turn angle must be between 0 and 360 degrees, got 400.0
  3. Speed must be positive, got 0.0
  4. Wait duration must be positive, got 0.0
  5. Repeat count must be at least 1, got 0
```

---

## 🔧 Troubleshooting

### Problema: `ModuleNotFoundError: No module named 'antlr4'`

**Solução:**
```powershell
pip install antlr4-python3-runtime
```

### Problema: `ModuleNotFoundError: No module named 'RoboLangLexer'`

**Solução:** Gerar os arquivos ANTLR:
```powershell
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o src RoboLang.g4
```

### Problema: Erro de sintaxe no arquivo `.robo`

**Solução:**
- Verifique se todos os comandos terminam corretamente
- Confirme que as chaves `{}` estão balanceadas
- Use apenas comandos válidos (`mover`, `virar`, `velocidade`, `esperar`, `repetir`)

### Problema: Script não encontrado

**Solução:**
Certifique-se de estar no diretório correto e use `src.` como prefixo:
```powershell
cd C:\Users\gwgus\Documents\Compiladores_E01_Grupo5
python -m src.demo_semantic
```

---

## 📚 Exemplos de Uso Rápido

### Criar e Testar um Novo Exemplo

```powershell
# 1. Criar arquivo
cd exemplos
echo "robo teste { mover x 10 cm }" > meu_teste.robo

# 2. Converter para AST
cd ..
python -m src.convert_examples

# 3. Validar semanticamente
python -m src.demo_semantic
```

### Verificar se um Exemplo é Válido

```powershell
# Edite demo_semantic.py e adicione seu exemplo:
# analyze_example(
#     "Meu teste",
#     """robo meuTeste {
#   mover x 20 cm
# }"""
# )

python -m src.demo_semantic
```

---

## 🎯 Resumo dos Comandos Principais

```powershell
# Demonstração completa
python -m src.demo_semantic

# Converter exemplos para JSON
python -m src.convert_examples

# Testar todos os exemplos
python -m src.test_semantic

# Regenerar parser (se alterar .g4)
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o src RoboLang.g4
```

---

**Desenvolvido para o projeto Compiladores_E01_Grupo5**  
**Linguagem:** RoboLang  
**Ferramentas:** Python 3.13, ANTLR 4.13.1

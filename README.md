# Compiladores_E01_Grupo5

# 🤖 Movimentos Precisos de Robôs Industriais



---

## 📝 Objetivo

- Implementar a análise semântica da linguagem RoboLang, verificando tipos, limites e
escopos dos comandos.
- Desenvolver a geração de código intermediário representando as instruções de
movimento.
- Criar um módulo de execução/simulação para demonstrar o funcionamento dos comandos
robóticos.
- Consolidar a documentação técnica e científica do compilador, conforme as normas da
ABNT.


---

## 🛠️ Linguagem e ferramentas utilizadas



* **Backend:** Python
* **Ferramentas** Visual Studio Code, PyCharm, ANTLR


---



### Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

* [Python](https://www.python.org/) (versão 3.14.0)
* [VScode](https://code.visualstudio.com/download)
* [ANTLR](https://www.antlr.org/download.html) (versão 4.13.1)

## 👨‍🏫 Instruções de execução

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




## 👥 Responsabilidades de cada integrante

**Heberth e Lucas** Documentação geral do projeto

**Gustavo** Implementação do modulo de execução para demonstrar o funcionamento dos comandos robóticos e Implementar a análise semântica da linguagem RoboLang.


## 🧾 Prints ou exemplos de saída

![image.png](attachment:de87195c-bd05-4e2c-b437-c40a3f17b301.png)

![image.png](attachment:ae80ef06-cf96-43ac-a79c-b6ed1ac9d37c.png)

![image.png](attachment:b5fb1ccd-1317-48df-9bd0-70d96c2448b7.png)
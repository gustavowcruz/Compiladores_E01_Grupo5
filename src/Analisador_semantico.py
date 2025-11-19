# ============================================================
# Analisador Semântico da Linguagem RoboLang
# Autor: Grupo 05
# Disciplina: Compiladores
# Professor(a): Ma. Layse Souza
# ============================================================

import datetime

class Simbolo:
    def __init__(self, nome, tipo, escopo):
        self.nome = nome
        self.tipo = tipo
        self.escopo = escopo

    def __repr__(self):
        return f"<Simbolo nome={self.nome}, tipo={self.tipo}, escopo={self.escopo}>"


class TabelaDeSimbolos:
    def __init__(self):
        self.tabela = []

    def adicionar_simbolo(self, simbolo):
        existente = next((s for s in self.tabela if s.nome == simbolo.nome and s.escopo == simbolo.escopo), None)
        if existente:
            raise Exception(f"Erro semântico: variável '{simbolo.nome}' já declarada no escopo '{simbolo.escopo}'.")
        self.tabela.append(simbolo)

    def buscar_simbolo(self, nome, escopo):
        for simbolo in reversed(self.tabela):
            if simbolo.nome == nome and simbolo.escopo == escopo:
                return simbolo
        for simbolo in reversed(self.tabela):
            if simbolo.nome == nome:
                return simbolo
        raise Exception(f"Erro semântico: variável '{nome}' não declarada no escopo '{escopo}'.")

    def __repr__(self):
        return "\n".join(str(s) for s in self.tabela)


class AnalisadorSemantico:
    def __init__(self):
        self.tabela_simbolos = TabelaDeSimbolos()
        self.escopo_atual = "global"
        self.erros_semanticos = []  # Lista de erros detectados

    def registrar_erro(self, mensagem):
        """Registra o erro na lista e grava no arquivo de log."""
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        erro_formatado = f"[{data_hora}] {mensagem}"
        self.erros_semanticos.append(erro_formatado)

        with open("erros_semanticos.log", "a", encoding="utf-8") as arquivo:
            arquivo.write(erro_formatado + "\n")

        print(f"❌ {mensagem}")

    def entrar_escopo(self, nome_escopo):
        self.escopo_atual = nome_escopo

    def sair_escopo(self):
        self.escopo_atual = "global"

    def declarar_variavel(self, nome, tipo):
        try:
            simbolo = Simbolo(nome, tipo, self.escopo_atual)
            self.tabela_simbolos.adicionar_simbolo(simbolo)
            print(f"✔ Variável declarada: {nome} ({tipo}) no escopo {self.escopo_atual}")
        except Exception as e:
            self.registrar_erro(str(e))

    def verificar_variavel(self, nome):
        try:
            simbolo = self.tabela_simbolos.buscar_simbolo(nome, self.escopo_atual)
            print(f"🔍 Variável '{nome}' encontrada: tipo {simbolo.tipo}, escopo {simbolo.escopo}")
        except Exception as e:
            self.registrar_erro(str(e))

    def atribuir_valor(self, nome, valor, tipo_valor):
        try:
            simbolo = self.tabela_simbolos.buscar_simbolo(nome, self.escopo_atual)
            if simbolo.tipo != tipo_valor:
                raise Exception(
                    f"Erro semântico: tipo incompatível na atribuição. "
                    f"Esperado '{simbolo.tipo}', obtido '{tipo_valor}'."
                )
            print(f"✅ Atribuição válida: {nome} = {valor} ({tipo_valor})")
        except Exception as e:
            self.registrar_erro(str(e))


# ============================================================
# Exemplo de Uso
# ============================================================
if __name__ == "__main__":
    analisador = AnalisadorSemantico()

    analisador.declarar_variavel("velocidade", "inteiro")
    analisador.declarar_variavel("velocidade", "inteiro")  # erro: duplicada
    analisador.declarar_variavel("eixo", "texto")

    analisador.entrar_escopo("movimento1")
    analisador.declarar_variavel("angulo", "real")

    analisador.atribuir_valor("velocidade", 100, "inteiro")
    analisador.atribuir_valor("angulo", "alto", "texto")  # erro: tipo inválido
    analisador.verificar_variavel("tempo")  # erro: variável inexistente

    analisador.sair_escopo()

    print("\n📘 Tabela de Símbolos Final:")
    print(analisador.tabela_simbolos)

    if analisador.erros_semanticos:
        print("\n⚠️ Erros semânticos detectados e registrados em 'erros_semanticos.log':")
        for erro in analisador.erros_semanticos:
            print(" -", erro)

from rich import print


class Caneta:
    """
    Classe Caneta

    Simula o funcionamento de uma caneta colorida.
    """

    def __init__(self, cor: str):
        self.cor = cor
        self.tampada = True

        self.cores = {
            "vermelha": "red",
            "azul": "blue",
            "verde": "green",
            "amarela": "yellow",
            "preta": "black",
            "branca": "white"
        }

    def destampar(self):
        self.tampada = False

    def escrever(self, texto: str):
        cor = self.cores[f"{self.cor.lower()}"]

        if self.tampada:
            print(f":no_entry_sign: A [{cor}]caneta[/{cor}] está tampada!")
            return

        print(f"[{cor}]{texto}[/{cor}]", end="")

    def quebrar_linha(self, linhas: int = 1):
        for _ in range(linhas + 1):
            print("")


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

# c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")

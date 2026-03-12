from rich import print
from rich.panel import Panel
from rich.text import Text


class Produto:
    """
    Classe Produto

    Cria a etiqueta de um produto com seu nome e valor.
    """

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self) -> Panel:

        valor = f"R${self.preco:,.2f}"

        texto = Text(f"{self.nome} "
                     f"{'-' * 30} "
                     f"{valor:.^30}",
                     justify="center"
        )
        etiqueta = Panel(texto, title="Produto", width = 35)

        print(etiqueta)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()

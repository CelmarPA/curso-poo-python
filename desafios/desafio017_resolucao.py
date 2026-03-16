from rich import print
from rich.panel import Panel
from rich.text import Text


class Produto:

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self) -> Panel:
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"

        etiqueta = Panel(conteudo, title="Produto", width=34)

        print(etiqueta)

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()

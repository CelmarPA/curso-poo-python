from rich import print
from rich.panel import Panel


class Churrasco:
    """
    Classe Churrasco

    Com método para analisar valor total, quantidade de carne e valor por pessoas.
    """

    def __init__(self, titulo: str, pessoas: int):
        # Consumo por pessoa 400g
        # Preço: R$ 82,40 / Kg

        self.titulo = titulo
        self.pessoas = pessoas

        self.preco_por_quilo: float = 82.40
        self.consumo: float = 0.4

    def analisar(self):
        quant_carne: float = self.pessoas * self.consumo
        custo_total: float = self.preco_por_quilo * quant_carne
        custo_por_pessoa: float = custo_total / self.pessoas

        texto = (f"Analisando {self.titulo} com [blue]{self.pessoas} convidados[/blue]\n"
                 f"Cada participante comerá {self.consumo}Kg e cada Kg custa R${self.preco_por_quilo:,.2f}\n"
                 f"Recomendo [blue]comprar {quant_carne:.3f}Kg[/blue] de carne\n"
                 f"O custo total será de [green]R${custo_total:,.2f}[/green]\n"
                 f"Cada pessoa pagará [yellow]R${custo_por_pessoa:,.2f}[/yellow] para participar.")

        analise = Panel(texto, title=f"{self.titulo}", width=80)

        print(analise)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

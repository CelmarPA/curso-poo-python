from rich import print
from rich.panel import Panel


class Churrasco:
    # Atributos de Classe
    consumo_padrão: float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg: float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, titulo, quant):
        # Atributos de instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self) -> str:
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrão

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/green] com [blue]{self.participantes} convidados[/blue]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrão}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():.3f}KG[/blue] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_individual():,.2f}[/green]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/yellow]"

        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

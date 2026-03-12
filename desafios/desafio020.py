from rich import print
from rich.panel import Panel


class Gamer:
    """
    Classe Gamer

    A classe possuí um método para mostra a ficha do gamer.
    """

    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, game: str):
        self.jogos_favoritos.append(game)
        self.jogos_favoritos.sort()

        return self.jogos_favoritos

    def ficha(self):
        favoritos = f"Jogos favoritos:"

        for game in self.jogos_favoritos:
            favoritos += f"\n:video_game: [blue]{game}[/blue]"

        texto = (f"Nome real: [black on blue]{self.nome}[/black on blue]\n"
                 f"{favoritos}")

        ficha = Panel(texto, title=f"Jogador <{self.nick}>", width=50)

        print(ficha)


j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros.")
j2.add_favoritos("Call of Duty")
j2.ficha()

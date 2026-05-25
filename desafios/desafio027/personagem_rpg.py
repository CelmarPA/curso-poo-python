import random
from abc import ABC, abstractmethod
from rich import print
from rich.table import Table


class Personagem(ABC):

    def __init__(self, nome: str, vida: int):
        self.nome: str = nome
        self.vida: int = vida
        self.golpes: list[str] = []


    def atacar(self, alvo: Personagem, forca: int  = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe: str = self.golpes[random.randrange(0, len(self.golpes))]

            print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força {forca}")

            alvo.receber_dano(forca)

        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer!")


    def receber_dano(self, dano: int):
        fator: int = random.randint(0, dano)
        self.vida -= fator

        if self.vida < 0:
            self.vida = 0

        print(f"[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]!")

    @abstractmethod
    def curar(self):
        pass

    def status_jogo(self):
        tabela = Table(title="Status dos Personagem")
        tabela.add_column("Nome")
        tabela.add_column("Vida")
        tabela.add_column("Golpes")

        golpes = ", ".join(self.golpes)

        tabela.add_row(f"{self.nome}", f"{self.vida}", f"{golpes}")

        print(tabela)


class Guerreiro(Personagem):

    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)

        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator

        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida.")


class Mago(Personagem):

    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)

        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator

        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {fator} pontos[/] de vida.")

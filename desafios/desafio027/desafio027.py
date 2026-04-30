from abc import ABC, abstractmethod


class Personagem(ABC):

    def __init__(self, nome: str, vida: int):
        self.nome: str = nome
        self.vida: int = vida


    def atacar(self, alvo, forca):
        pass

    def receber_dano(self, dano):
        pass

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)


    def curar(self):
        pass


class Mago(Personagem):

    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)

    def curar(self):
        pass
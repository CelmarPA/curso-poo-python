from pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome: str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo: str = cargo
        self.setor: str = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")
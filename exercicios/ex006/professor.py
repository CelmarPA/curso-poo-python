from pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade: str = especialidade
        self.nivel: str = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")
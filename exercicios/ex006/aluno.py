from pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, nome: str, idade: int, curso: str, turma: str):
        super().__init__(nome, idade)
        self.curso: str = curso
        self.turma: str = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula")
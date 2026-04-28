from rich import inspect

class Pessoa:

    def __init__(self, nome: str = "", idade: int = 0):
        self.nome: str = nome
        self.idade: int = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):

    def __init__(self, nome: str, idade: int, curso: str, turma: str):
        super().__init__(nome, idade)
        self.curso: str = curso
        self.turma: str = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula")


class Professor(Pessoa):

    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str):
        super().__init__(nome, idade)
        self.especialidade: str = especialidade
        self.nivel: str = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")


class Funcionario(Pessoa):

    def __init__(self, nome: str, idade: int, cargo: str, setor: str):
        super().__init__(nome, idade)
        self.cargo: str = cargo
        self.setor: str = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")


a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Claúdia", 27, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)
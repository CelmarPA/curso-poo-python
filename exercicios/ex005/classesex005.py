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
from rich import print
from rich import inspect


class Funcionario:
    # Atributos de classe
    empresa = "Curso em Vídeo"

    def __init__(self,nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou [blue]{self.nome}[/blue], e sou {self.cargo} fo setor de {self.setor} da empresa {self.__class__.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

# inspect(c1, methods=True)

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())

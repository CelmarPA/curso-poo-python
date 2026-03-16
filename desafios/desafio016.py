from rich import print
from rich import inspect


class Funcionario:
    """
    Classe Funcionario, cadastra o funcionário com nome, setor e cagor.

    Tem como métodos apresentacao, que apresenta o funcionário e __str__ que define o funcionário.
    """

    empresa = "Curso em Vídeo"

    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo



    def apresentacao(self) -> str:
        return (f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da "
                f"empresa {self.__class__.empresa}.")

    def __str__(self) -> str:
        return f"Funcionário {self.nome} do setor {self.setor} ocupa o cargo {self.cargo} na empresa {Funcionario.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

# inspect(c1, methods=True)

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())

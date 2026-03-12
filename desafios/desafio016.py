from rich import print


class Funcionario:
    """
    Classe Funcionario, cadastra o funcionário com nome, setor e cagor.

    Tem como métodos apresentacao, que apresenta o funcionário e __str__ que define o funcionário.
    """

    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

        self.empresa = "Curso em Vídeo"

    def apresentacacao(self):
        return (f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da "
                f"empresa {self.empresa}.")

    def __str__(self):
        return f"Funcionário {self.nome} do setor {self.setor} ocupa o cargo {self.cargo} na empresa {self.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacacao())

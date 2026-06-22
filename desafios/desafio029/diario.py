from rich import print


class Diario:

    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        return PermissionError("Ninguém tem permissão de ver a senha")

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha = None):
        if not senha or senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")

        print("[green]Diário LIBERADO![/]")

        for msg in self.__segredos:
            print(f"- {msg}")

from rich import print


class Diario:

    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha")

    @senha.setter
    def senha(self, nova_senha):
        senha_atual = input("Informe sua senha atual: ")

        if senha_atual == self.__senha:
            self.__senha = nova_senha

            print("A senha foi alterada com sucesso.")

        else:
            raise PermissionError("Senha inválida...")

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha = None):
        if not senha or senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")

        print("[green]Diário LIBERADO![/]")

        for msg in self.__segredos:
            print(f"- {msg}")

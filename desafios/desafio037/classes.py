from rich import print
from rich.panel import Panel


class Mensagem:

    def __init__(self, msg:str = "", tipo:str = "aviso", icone:str = ":speech_balloon:"):
        self.__mensagem = None
        self.__tipo = None
        self.__icone = None

        self.mensagem = msg
        self.tipo = tipo
        self.icone = icone

    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, txt):
        self.__mensagem = txt

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def icone(self):
        return self.__icone

    @icone.setter
    def icone(self, icone):
        self.__icone = icone

    def mostrar(self):
        msg = Panel(
            self.mensagem,
            title=f"{self.icone} {self.tipo.upper()} {self.icone}",
            style="#ffffff on #000000",
            width=50
        )

        print(msg)


class Alerta(Mensagem):

    def __init__(self, msg:str = ""):
        super().__init__(msg, "alerta", ":warning:")

    def mostrar(self):
        msg = Panel(
            self.mensagem,
            title=f"{self.icone} {self.tipo.upper()} {self.icone}",
            style="#000000 on #fffc1b",
            width=50
        )

        print(msg)


class Erro(Mensagem):

    def __init__(self, msg:str = ""):
        super().__init__(msg, "erro", ":prohibited:")

    def mostrar(self):
        msg = Panel(
            self.mensagem,
            title=f"{self.icone} {self.tipo.upper()} {self.icone}",
            style="#ffff00 on #880000",
            width=50
        )

        print(msg)

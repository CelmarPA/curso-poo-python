from abc import ABC, abstractmethod


class Arquivo(ABC):

    def __init__(self, nome:str, extensao:str, tamanho:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho / 1_000_000
        self.extensao = extensao
        self.nome_completo = f"{self.nome}{self.extensao} ({self.tamanho}MB)"

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = [".pdf", ".doc", ".docx"]
        ext = ext.lower().strip()

        if ext in formatos:
            self._extensao = ext

        else:
            raise AttributeError("O arquivo está em um formato não suportado")

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, ".pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Adobe Reader'")


class DOC(Arquivo):

    def __init__(self, nome, tamanho):
        super().__init__(nome, ".docx", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Microsoft Word'")


def abrir_arquivo(arquivo):
    try:
        arquivo.abrir()

    except e:
        print("Não foi possivel abrir o arquivo")

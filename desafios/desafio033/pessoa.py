from abc import ABC
from datetime import datetime


class Pessoa(ABC):

    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if not 1926 < ano < datetime.now().year:
            raise ValueError(f"Ano {ano} é inválido")

        self._nascimento = ano

    @property
    def idade(self):
        ano_atual = datetime.now().year

        return ano_atual - self.nascimento

    @idade.setter
    def idade(self, idade):

        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")

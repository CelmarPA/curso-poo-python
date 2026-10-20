from abc import ABC, abstractmethod
import re


class Validador(ABC):

    @abstractmethod
    def validar(self, valor: str):
        pass
        "Valor: gustavo é válido? SIM"


class Usuario(Validador):

    """
    5 a 20 caracteres
    letras minusculas
    numeros
    simbolos de sublinhado
    """

    def validar(self, valor: str) -> bool:

        if re.fullmatch(r"^[a-z0-9_]{5,20}$", valor):
            return True

        else:
            return False


class Email(Validador):
    """
    Deve conter uma única @
    usuário pode conter, letras, números, e alguns simbolos
    os dominios contem pontos
    tdl encerra com ponto e pelo menos 2 letras
    """

    def validar(self, valor: str) -> bool:

        if re.fullmatch(r"^[a-z0-9_]+@([a-z0-9_]+\.)+[a-z]{2,}$", valor):
            return True

        else:
            return False


class Senha(Validador):

    """
    Pelo menos 8 characteres
    pelo menos uma letra maiúscula
    pelo menos um símbolo
    """

    def validar(self, valor: str) -> bool:

        if re.fullmatch(r'(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>/?]).{8,}', valor):
            return True

        else:
            return False


def validar_dado(validador, valor):
    resultado = validador.validar(valor)

    print(f"Valor: {valor} é válido? {'SIM' if resultado else 'NÃO'}")

class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self) -> str:
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self) -> int|float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito")

    def __eq__(self, other: object) -> bool:
        if self.__saldo == other.__saldo:
            return True

        else:
            return False

    def __iadd__(self, valor: int|float) -> object:
        self.__saldo += valor

        return self

    def __isub__(self, valor: int|float) -> object:
        self.__saldo -= valor

        return self

    def __le__(self, other: object) -> bool:
        if self.__saldo <= other.__saldo:
            return True

        else:
            return False

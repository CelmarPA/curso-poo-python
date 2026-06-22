import hashlib
import pwinput

class ContaBancaria:

    def __init__(self, id, titular, saldo=0, chave=None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo

        if not chave:
            chave = self.pede_senha()

        self.__hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()

        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        chave = self.pede_senha()

        if not self.validar_senha(chave):
            print("Senha inválida")

            return

        if not nome:
            print("Digite um nome válido")

            return

        self._titular = nome
        print(f"Nome do titular alterado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor para despoisto deve ser maior que zero")

        self.__saldo += valor

        print(f"Depósito de R${valor:,.2f} autorizado no conta {self._id}")

    @staticmethod
    def pede_senha() -> str:
        chave = pwinput.pwinput(prompt="Senha: ", mask="*")

        return chave

    def sacar(self, valor:float, chave: str = None):
        if not chave:
            chave = self.pede_senha()

        if not self.validar_senha(chave):
            print("Senha não confere. Saque não autorizado!")

            return

        if valor <= 0:
            print("Valor do saque deve ser maior que 0")

            return

        if valor > self.__saldo:
            print("Valor do saque deve ser menor ou igual ao saldo")

            return

        self.__saldo -= valor

        print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")

    def validar_senha(self, chave: str) -> bool:
        chave_hash= hashlib.sha256(chave.encode("utf-8")).hexdigest()

        if chave_hash == self.__hash:
            return True

        return False
import hashlib


class ContaBancaria:

    def __init__(self, conta_id:int, titular:str, saldo:int|float=0, chave=None):
        self._id = conta_id
        self._titular = titular
        self.__saldo = saldo

        if not chave:
            chave = self.pede_senha()

        self.__hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()

        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    @staticmethod
    def pede_senha() -> str:

        from pwinput import pwinput

        chave = pwinput(prompt="Senha: ", mask="*")

        return chave

    def validar_senha(self, chave: str) -> bool:

        chave_hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()

        if chave_hash == self.__hash:
            return True

        return False

    def __str__(self) -> str:
        return f"Estado atual da conta: {self.__dict__}"

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome: str):
        chave = self.pede_senha()

        if not self.validar_senha(chave):
            print("Senha inválida")

            return

        if not nome:
            print("Digite um nome válido")

            return

        self._titular = nome
        print(f"Nome do titular alterado com sucesso.")

    def depositar(self, valor:int|float):
        if valor <= 0:
            raise ValueError("Valor para despoisto deve ser maior que zero")

        self.__saldo += valor

        print(f"Depósito de R${valor:,.2f} autorizado no conta {self._id}")

    def sacar(self, valor:int|float, chave: str | None = None):
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


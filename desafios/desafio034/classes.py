from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome:str = None, salario:int|float = 1_621):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self) -> int|float:
        return self.__salario

    @salario.setter
    def salario(self, valor: int|float=None) -> None:
        if valor is None:
            raise ValueError("Impossível reajusta o salário desse jeito!")

        else:
            if valor > self.__salario:
                self.__salario = valor

            else:
                raise ValueError("Você não pode reduzir o sálario de um funcionário.")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self) -> str:
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}"


class Gerente(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self): # Bônus 15%
        return self.salario * 0.15


class Designer(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self): # Bônus 8%
        return self.salario * 0.08


class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):  # Bônus 10%
        return self.salario * 0.10

from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):

    def __init__(self, lados: int) -> None:
        self.qtd_lados: int = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado: float = 1) -> None:
        super().__init__(4)
        self.lado: float = lado

    def perimetro(self) -> float | int:
        return self.lado * 4

    def area(self) -> float | int:
        return self.lado ** 2


class Circulo(Poligono):

    def __init__(self, raio: float = 1) -> None:
        super().__init__(0)
        self.raio: float = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio

    def area(self) -> float:
        return pi * self.raio ** 2

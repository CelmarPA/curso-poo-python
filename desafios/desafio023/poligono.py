from abc import ABC, abstractmethod


class Poligono(ABC):

    def __init__(self, qtd_lados: int) -> None:
        self.qtd_lados: int = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado: float | int) -> None:
        super().__init__(4)
        self.lado: float = lado

    def perimetro(self) -> float | int:
        return self.lado * 4

    def area(self) -> float | int:
        return self.lado ** 2


class Circulo(Poligono):

    def __init__(self, raio: float) -> None:
        super().__init__(0)
        self.raio: float = raio

    def perimetro(self) -> float:
        return 2 * 3.14159 * self.raio

    def area(self) -> float:
        return 3.14159 * self.raio ** 2

from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia: float = 0, frete: float = 0) -> None:
        self.distancia: float = distancia
        self.frete: float = frete

    @abstractmethod
    def calcular_frete(self) -> float:
        pass


class Moto(Transporte):
    fator: float = 0.50

    def __init__(self, distancia: float) -> None:
        super().__init__()
        self.distancia: float = distancia

    def calcular_frete(self) -> float:
        frete = self.distancia * Moto.fator

        return f"R${frete:.2f}"


class Caminhao(Transporte):
    fator: float = 1.20

    def __init__(self, distancia: float) -> None:
        super().__init__()
        self.distancia: float = distancia

    def calcular_frete(self) -> str | None:
        if self.distancia < 50:
            return "Raio mínimo de 50 Km."

        frete = self.distancia * Caminhao.fator

        return f"R${frete:.2f}"

class Drone(Transporte):
    fator: float = 9.50

    def __init__(self, distancia: float) -> None:
        super().__init__()
        self.distancia: float = distancia

    def calcular_frete(self) -> str | None:
        if self.distancia > 10:
            return "Raio máximo de 10km."

        frete = self.distancia * Drone.fator

        return f"R${frete:.2f}"

from rich import inspect, print
from poligono import *


def main() -> None:
    p1 = Circulo(20)

    print(f"Perímetro = {p1.perimetro():.1f}")
    print(f"Área = {p1.area():.1f}")


if __name__ == "__main__":
    main()
from rich import print, inspect
from poligono import *


def main():
    q = Quadrado(20)
    # inspect(q, methods=4)
    print(f"Um quadrado de lado {q.lado} tem perímetro de {q.perimetro()} cm")
    print(f"Um quadrado de lado {q.lado} tem área de {q.area()} cm²")

    c= Circulo(12)
    # inspect(c, methods=4)
    print(f"Um circulo de raio {c.raio} tem perímetro de {c.perimetro():.1f} cm")
    print(f"Um circulo de raio {c.raio} tem área de {c.area():.1f} cm²")


if __name__ == "__main__":
    main()
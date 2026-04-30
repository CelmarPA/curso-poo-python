from rich import print
from transportadora import *
from rich.table import Table


def main() -> None:
    dist = 100

    viagem: list[Transporte] = [Moto(dist), Caminhao(dist), Drone(dist)]

    table: Table = Table(title="Tabela de Fretes")
    table.add_column("Distância", justify="left")
    table.add_column("Tipo", justify="left")
    table.add_column("Frete", justify="left")

    for transporte in viagem:
        table.add_row(f"{dist}Km", f"{type(transporte).__name__}", f"{transporte.calcular_frete()}")

    print(table)


if __name__ == "__main__":
    main()

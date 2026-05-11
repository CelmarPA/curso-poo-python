from transportes import *
from rich import print, inspect
from rich.table import Table


def main():
    dist = 10

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    # entrega = Drone(dist)
    # print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()

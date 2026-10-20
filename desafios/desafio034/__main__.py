from classes import *


def main():
    f = Gerente("Pedro", 12_000)
    print(f)

    f.salario = 15_000
    print(f)

    print(f.calcular_bonus())


if __name__ == "__main__":
    main()

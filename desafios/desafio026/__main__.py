from funcionarios import *


def main() -> None:
    f1 = FuncionarioHorista("Paulo", 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioMesalista("Amanda", 9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
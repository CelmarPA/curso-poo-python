from rich import inspect
from funcionarios import *


def main():
    f1 = FuncionarioMensalista("José da Silva", 8500)
    f2 = FuncionarioHorista("Maria de Souza", 25, 250)

    f1.calcular_salario()
    f1.analisar_salario()
    f2.calcular_salario()
    f2.analisar_salario()

    # inspect(f1)


if __name__ == "__main__":
    main()

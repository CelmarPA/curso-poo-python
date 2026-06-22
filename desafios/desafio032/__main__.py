from banco import ContaBancaria
from rich import print, inspect


def main():
    print("Criando a conta...")
    cc = ContaBancaria(123, "Gustavo", 1000, "Gafanhoto")

    print("Realizando depósito")
    cc.depositar(500)

    print("Realizando saque")
    cc.sacar(200, "Gafanhoto")

    cc.nome = "Manuel"

    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
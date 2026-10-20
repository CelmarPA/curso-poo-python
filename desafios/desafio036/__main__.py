from classes import *


def main():
    finalizar_compra(Pix(), 1_500)
    finalizar_compra(CartaoCredito(), 9_540.84)
    finalizar_compra(Boleto(), 439.23)

if __name__ == "__main__":
    main()

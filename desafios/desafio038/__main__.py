from classes import *


def main():
    p1 = Produto("Mouse", 325)
    p2 = Produto("Teclado", 433)
    p3 = Produto("Memória 256", 1_800)
    p4 = Produto("Placa de vídeo", 25_999)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p3 + p4

    c2 = c2 + c1 + p2

    print(c1)
    print(c2)

if __name__ == "__main__":
    main()

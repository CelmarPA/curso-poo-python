from classes import *


def main():
    u = [
        Usuario("Pedro", "pedro@gmail.com"),
        Usuario("Maria", "mariazinha@hotmail.com")
    ]

    a = [
        Aluno("Cláudia", "ADS", "2 per"),
        Aluno("Ana", "Adm", "4 per"),
        Aluno("Mario", "Seg", "1 per")
    ]

    exportar_dados(JSON(), u)
    exportar_dados(JSON(), a)

    exportar_dados(XML(), u)
    exportar_dados(XML(), a)

if __name__ == "__main__":
    main()

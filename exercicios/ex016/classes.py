class Porta:

    def abrir(self):
        print("Girar a maçaneta e empurrar/puxar a porta")


class Empresa:

    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")


class Ovo:

    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes sobre um frigideira")


class Pedra:
    pass


# Método Pythonico Polimorfico DUCK TYPING

def tentar_abrir(objeto):

    try:
        objeto.abrir()

    except:
        print(f"Encontrei problemaas ao tentar abrir objeto do tipo {objeto.__class__.__name__}")

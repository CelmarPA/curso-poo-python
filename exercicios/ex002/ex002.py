# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use
    variável = Gafanhoto(nome, idade)
    """

    def __init__(self, n = "", i = 0):  # Método Construtor
        # Atributos de Instância
        self.nome = n
        self.idade = i

    # Método de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objeto
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)
print(g1.__dict__)  # Attribute
print(g1.__getstate__())  # Method
print(g1.__class__)
print(g1.__doc__) # Dunder Attribute

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)
print(g2.__getstate__())  # Method

g3 = Gafanhoto()
print(g3)
print(g3.__getstate__())  # Method

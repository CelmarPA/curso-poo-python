class Retangulo:

    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para base")

        self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para altura")

        self._altura = valor

    @property
    def medidas(self):
        return f"Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @medidas.setter
    def medidas(self, medidas):
        for medida in medidas:
            if medida <= 0:
                raise ValueError("Valor inválido para medidas")

        self._base = medidas[0]
        self._altura = medidas[1]

    @property
    def area(self):
        self._area = self._base * self._altura

        return self._area

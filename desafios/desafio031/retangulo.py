class Retangulo:

    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da base deve ser um número.")

        if valor <= 0:
            raise ValueError("Valor inválido para base")

        self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da altura deve ser um número.")

        if valor <= 0:
            raise ValueError("Valor inválido para altura")

        self._altura = valor

    @property
    def medidas(self):
        return f"Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @medidas.setter
    def medidas(self, medidas:tuple):

        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla.")

        if len(medidas) != 2:
            raise SyntaxError("Informe uma tupla com apenas dois valores numéricos.")

        for medida in medidas:
            if medida <= 0:
                raise ValueError("Valor inválido para medidas")

        if isinstance(medidas[0], float) or isinstance(medidas[0],  int):
            self.base = medidas[0]

        else:
            raise TypeError("A base deve ser um número.")

        if isinstance(medidas[1], float) or isinstance(medidas[1],  int):
            self.altura = medidas[1]

        else:
            raise TypeError("A altura deve ser um número.")

    @property
    def area(self):
        self._area = self._base * self._altura

        return self._area

    @area.setter
    def area(self, value):
        raise PermissionError("Área não pode ser configurada desse jeito.")

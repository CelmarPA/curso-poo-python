class Termostato:

    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16:
            self.__temperatura = 16

        elif valor > 30:
            self.__temperatura = 30

        else:
            if isinstance(valor, int):
                self.__temperatura = valor

            else:
                if valor % 10 == 0.5:
                    self.__temperatura = valor

                else:
                    raise ValueError(f"Temperatura de {valor}°C é inválida!")

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"

from abc import ABC, abstractmethod
import locale


class Pagamento(ABC):

    def __init__(self):
        self.__valor = 0

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self.__valor = valor

        else:
            raise ValueError(f"O pagamento só pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

        return locale.currency(self.valor, grouping=True, symbol=True)

    @abstractmethod
    def pagar(self, valor:int|float):
        pass


class Boleto(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self, valor:int|float):
        try:
            self.valor = valor

            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto"

        except Exception as e:
            return f"Falha no pagamento de {self.valor} via Boleto!"



class Pix(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self, valor:int|float):
        try:
            self.valor = valor

            return f"Pagamento CONFIRMADO de {self.fvalor} via Pix"

        except Exception as e:
            return f"Falha no pagamento de {self.valor} via Pix!"


class CartaoCredito(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self, valor:int|float):
        try:
            self.valor = valor

            return f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito"

        except Exception as e:
            return f"Falha no pagamento de {self.valor} via Cartão de Crédito!"


def finalizar_compra(tipo_pag: Pagamento, valor: int|float):
    try:
        print(tipo_pag.pagar(valor))

    except e:
        print("Não foi possível realizar o pagamento!")

import locale


locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


class Produto:

    def __init__(self, nome: str= "", preco:int|float = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:

        preco = locale.currency(self.preco, grouping=True, symbol=True)

        return f"{self.nome} ({preco})"


class Carrinho:

    def __init__(self):
        self.produtos = []
        self.total = 0

    def __add__(self, other: object):
        if isinstance(other, Carrinho):
            novo_carrinho = Carrinho()

            novo_carrinho.produtos = self.produtos + other.produtos
            novo_carrinho.total = self.total + other.total

            return novo_carrinho

        elif isinstance(other, Produto):
            self.produtos.append(other)
            self.total += other.preco

            return self

        raise TypeError("Só é possível somar um Carrinho com um Produto ou com outro Carrinho.")

    def __str__(self) -> str:
        total = locale.currency(self.total, grouping=True, symbol=True)
        f_total = f"Total: {total}"

        produtos = ""

        for produto in self.produtos:
            produtos += f"{produto}\n"

        resumo = (f"{'-' * 30}\n"
                  f"{produtos}"
                  f"{'-' * 30}\n"
                  f"Total: {f_total}\n")

        return resumo

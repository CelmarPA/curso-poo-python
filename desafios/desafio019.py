from rich import print
from time import sleep

class Livro:
    """
    Classe Livro

    Simula passagem de paginas e informa se o usuário chegou ao final do livro.
    """

    def __init__(self, titulo: str, paginas: int):
        self.titulo = titulo
        self.paginas = paginas

        self.pagina_atual: int = 1

        self.abrir_livro()

    def abrir_livro(self):
        print(f":open_book: [blue] Você acabou de abrir o livro '[red]{self.titulo}[/red]' que tem "
              f"[green]{self.paginas} páginas[/green] no total. Você agora está na [yellow]página "
              f"{self.pagina_atual}[/yellow][/blue]")

    def avancar_paginas(self, quant_paginas):
        count_pag = 0

        for _ in range(quant_paginas):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                count_pag += 1

                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                sleep(0.5)

            else:
                break

        print(f"[blue]Você avançou {count_pag} páginas e agora está na [yellow]página {self.pagina_atual}[/yellow][/blue]")

        if self.pagina_atual == self.paginas:
            print(f":closed_book: [red] Você chegou ao final do livro '{self.titulo}'[/red]")


l1= Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)

from rich.panel import Panel
from rich.bar import Bar
from rich.console import Group
from rich.columns import Columns
from rich.console import Console


class ControleRemoto:
    """
    Classe ControleRemoto

    Simula o funcionamento de um controle remoto simples.
    """

    def __init__(self):
        self.console = Console()

        self.ligada: bool = False
        self.canal: int = 1
        self.volume: int = 1
        self.texto: Group = Group(":no_entry_sign: [red]A TV está desligada[/red]")

        self.canal_atual = ""
        self.volume_atual= ""

        self.atualizar_canal()
        self.atualizar_volume()

    def controle(self):
        while True:
            self.console.clear()

            if self.ligada:
                self.texto = Group(
                    f"CANAL  = {self.canal_atual}",
                    Columns(["VOLUME =", self.volume_atual], padding=(0,1))
                )

            tv = Panel(self.texto, title="[ TV ]", width=30, expand=False)

            self.console.print(tv)

            option = self.console.input(f"< CH{self.canal} >   - VOL{self.volume} + ")

            match option:
                case "0":
                    break

                case "@":
                    self.ligada = not self.ligada

                case "<":
                    if self.canal == 1:
                        self.canal = 5

                    else:
                        if self.ligada:
                            self.canal -= 1

                case ">":
                    if self.canal == 5:
                        self.canal = 1

                    else:
                        if self.ligada:
                            self.canal += 1

                case "-":
                    if self.volume == 1:
                        continue

                    else:
                        if self.ligada:
                            self.volume -= 1

                case "+":
                    if self.volume == 5:
                        continue

                    else:
                        if self.ligada:
                            self.volume += 1

            if not self.ligada:
                self.texto: Group = Group(":no_entry_sign: [red]A TV está desligada[/red]")

            self.atualizar_canal()
            self.atualizar_volume()

    def atualizar_canal(self):
        canais = ["1", "2", "3", "4", "5"]

        canais[self.canal - 1] = f"[on yellow]{self.canal}[/on yellow]"

        self.canal_atual = " ".join(canais)

    def atualizar_volume(self):
        barra_volume = Bar(5, 0, self.volume, width=5, bgcolor="white", color="cyan")

        self.volume_atual = barra_volume


c1 = ControleRemoto()
c1.controle()

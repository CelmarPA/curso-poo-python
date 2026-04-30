from rich import print
from rich.panel import Panel
from rich.text import Text

class ControleRemoto:
    """
    Classe ControleRemoto

    Simula o funcionamento de um controle remoto simples.
    """

    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 1) -> None:
        self.ligada: bool = False
        self.canal_atual: int = canal
        self.volume_atual: int = volume

    def liga_desliga(self) -> None:
        self.ligada = not self.ligada

    def canal_mais(self) -> None:
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min

            else:
                self.canal_atual += 1

    def canal_menos(self) -> None:
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max

            else:
                self.canal_atual -= 1

    def volume_mais(self) -> None:
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self) -> None:
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self) -> None:
        if not self.ligada:
            conteudo: Text = Text("🚫 A TV está desligada", style="bold red")

        else:
            conteudo = Text("CANAL = ")

            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo.append(f" {canal} ", style="black on yellow")
                else:
                    conteudo.append(f" {canal} ")

            conteudo.append("\nVOLUME = ")

            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo.append("█", style="cyan")

                else:
                    conteudo.append("█", style="white")

        tv: Panel = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

    def update(self) -> None:
        if self.ligada:
            comando: str = input(f"< CH{self.canal_atual} >    - VOL{self.volume_atual} + ")

        else:
            comando: str = input(f"< CH >    - VOL + ")

        match comando:
            case "0":
                return True

            case "@":
                c.liga_desliga()

            case ">":
                c.canal_mais()

            case "<":
                c.canal_menos()

            case "+":
                c.volume_mais()

            case "-":
                c.volume_menos()

        print("\n" * 10)

        return False


c = ControleRemoto()

while True:
    c.mostrar_tv()

    if c.update():
        break

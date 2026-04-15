# desafio022_resolucao.py

from rich import print
from rich.panel import Panel


class ControleRemoto:

    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 2) -> None:
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def liga_desliga(self) -> None:
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min

            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max

            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1


    def mostrar_tv(self) -> None:

        if not self.ligado:
            conteudo = ":prohibited: A TV está desligada"

        else:
            conteudo = "CANAL = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"

        tv: Panel = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)


c = ControleRemoto()

while True:
    c.mostrar_tv()

    comando: str = input(f"< CH{c.canal_atual} >    - VOL{c.volume_atual} + ")

    match comando:
        case "0":
            break

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

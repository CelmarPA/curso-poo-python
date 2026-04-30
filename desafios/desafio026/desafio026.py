from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    salario_minimo: int = 1612
    inss: float = 7.5

    def __init__(self, nome: str, salario: float) -> None:
        self.nome: str = nome
        self.salario: float = salario

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):

        quant_salarios = self.salario / Funcionario.salario_minimo

        text = (f"O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) é de "
                f"[green]R${self.salario:.2f}[/] e corresponde a [yellow]{quant_salarios:.1f} salários mínimos[/].")

        analise: Panel = Panel(title="Análise de Salário", renderable=text, width=50)
        print(analise)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome: str, valor_hora: float, horas_trabalhadas: int) -> None:
        self.valor_hora: float = valor_hora
        self.horas_trabalhadas: int = horas_trabalhadas
        self.salario: float = self.calcular_salario()

        super().__init__(nome, self.salario)

    def calcular_salario(self):
        salario_bruto = self.valor_hora * self.horas_trabalhadas
        salario = salario_bruto - (salario_bruto * FuncionarioHorista.inss / 100)

        return salario



class FuncionarioMesalista(Funcionario):

    def __init__(self, nome: str, salario_bruto: float) -> None:
        self.salario_bruto: float = salario_bruto
        self.salario: float = self.calcular_salario()

        super().__init__(nome, self.salario)

    def calcular_salario(self):
        salario = self.salario_bruto - (self.salario_bruto * FuncionarioMesalista.inss / 100)

        return salario


trab = FuncionarioHorista("Paulo", 12, 200)
trab.calcular_salario()
trab.analisar_salario()

trab = FuncionarioMesalista("Amanda", 9500)
trab.calcular_salario()
trab.analisar_salario()
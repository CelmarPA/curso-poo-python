import xml.etree.ElementTree as ET
import json


class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class JSON:

    def exportar(self, lista_objetos):
        lista_dicts = [dado.__dict__ for dado in lista_objetos]

        print(json.dumps(lista_dicts, indent=4, ensure_ascii=False))


class XML:

    def exportar(self, lista_objetos):

        raiz = ET.Element("dados")

        for objeto in lista_objetos:
            tag = ET.SubElement(raiz, objeto.__class__.__name__)

            for chave, valor in objeto.__dict__.items():
                ET.SubElement(tag, chave).text = valor

        ET.indent(raiz, space="    ")
        ET.dump(raiz)


def exportar_dados(exportador, dados):
    exportador.exportar(dados)

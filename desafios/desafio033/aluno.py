from pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")

        self._curso = curso
    def add_curso(self, curso: str):
        if curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)

        else:
            print(f"O curso {curso} já está na lista de cursos oficiais.")

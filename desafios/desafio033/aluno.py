from pessoa import Pessoa


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")

        self._curso = curso

    @staticmethod
    def add_curso(curso: str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <=5:
            if curso not in Aluno.cursos_oficiais:
                Aluno.cursos_oficiais.append(curso)

            else:
                print(f"O curso {curso} já está na lista de cursos oficiais.")

        else:
            raise ValueError(f"Nome {curso} está fora do padrão para Cursos!")

    def __str__(self) -> str:
        return f"O aluno {self._nome} está matriculado no curso de {self.curso}..."

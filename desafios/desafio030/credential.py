from hashlib import sha256


class Credencial:

    def __init__(self):
        self.__hash= None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        if len(senha) > 0:
            self.__hash = sha256(senha.encode("utf-8")).hexdigest()

        else:
            raise ValueError("Senha inválida")

    def validar(self, chave):
        senha_hash = sha256(chave.encode("utf-8")).hexdigest()

        if senha_hash == self.senha:
            print("Senha confere!")

            return True

        else:
            print("Senha não bate!")

            return False

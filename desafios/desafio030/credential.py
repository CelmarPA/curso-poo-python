import hashlib


class Credencial:

    def __init__(self):
        self.__hash= None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        hash_object = hashlib.sha256(senha.encode("utf-8"))

        self.__hash = hash_object.hexdigest()

    def validar(self, chave):
        senha_hash = hashlib.sha256(chave.encode("utf-8")).hexdigest()

        if senha_hash == self.senha:
            print("Senha confere!")

            return True

        else:
            print("Senha não bate!")

            return False

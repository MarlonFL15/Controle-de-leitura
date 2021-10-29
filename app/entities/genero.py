class Genero():
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def cliente(self, nome):
        self.__nome = nome

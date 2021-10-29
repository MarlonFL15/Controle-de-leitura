class Livro():
    def __init__(self, titulo, generos):
        self.__titulo = titulo
        self.__generos = generos

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def generos(self):
        return self.__generos

    @generos.setter
    def generos(self, generos):
        self.__generos = generos

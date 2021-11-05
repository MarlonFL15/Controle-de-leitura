class Leitura():
    def __init__(self, livro, nota, status, resenha):
        self.__livro = livro
        self.__nota = nota if nota else 0
        self.__status = status
        self.__resenha = resenha

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, livro):
        self.__livro = livro

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def resenha(self):
        return self.__resenha

    @resenha.setter
    def resenha(self, resenha):
        self.__resenha = resenha
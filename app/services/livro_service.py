from ..models import Livro

def getAll():
    return list(Livro.objects.values())

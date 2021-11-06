from ..models import Leitura

def getAll():

    return Leitura.objects.all()

def getById(id):
    return Leitura.objects.get(id=id)

def save(leitura):
    return Leitura.objects.create(livro = leitura.livro, nota = leitura.nota, status = leitura.status, resenha=leitura.resenha)


def update(old_leitura, new_leitura):
    old_leitura.livro = new_leitura.livro
    old_leitura.nota = new_leitura.nota
    old_leitura.status = new_leitura.status
    old_leitura.resenha = new_leitura.resenha
    old_leitura.save(force_update=True)

def delete(leitura):
    leitura.delete()



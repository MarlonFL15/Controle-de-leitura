from django.shortcuts import render, redirect
from .forms import LeituraForm
from .services import leitura_service, livro_service
from .entities import leitura
# Create your views here.
def leituras(request):
    leituras = list(leitura_service.getAll())
    for index in range(0, len(leituras)):
        leituras[index].generos = ', '.join([x.nome for x in list(leituras[index].livro.generos.all())])

    return render(request, 'leituras/leituras.html', {'leituras': leituras})

def cadastrar_leitura(request):
    form = LeituraForm()
    livros = livro_service.getAll()

    if request.method == "POST":
        form = LeituraForm(request.POST or None)

        if form.is_valid():
            nota = request.POST.get('rating')
            livro = form.cleaned_data['livro']
            resenha = form.cleaned_data['resenha']
            status = form.cleaned_data['status']
            leitura_novo = leitura.Leitura(nota=nota, status=status, resenha=resenha, livro=livro)
            leitura_service.save(leitura_novo)
            return redirect('leituras')

    return render(request, 'leituras/form.html', {
        'form': form,
        'livros': livros
    })

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, response
from django.shortcuts import render, redirect
from .forms import LeituraForm, UsuarioForm, LoginForm
from .services import leitura_service, livro_service, usuario_service
from .entities import leitura, usuario
# Create your views here.

def redirect_leituras(request):
    return redirect('leituras')

@login_required
def leituras(request):
    leituras = list(leitura_service.getByUser(request.user))
    for index in range(0, len(leituras)):
        leituras[index].generos = ', '.join([x.nome for x in list(leituras[index].livro.generos.all())])


    return render(request, 'leituras/leituras.html', {'leituras': leituras})

@login_required
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
            usuario = request.user
            leitura_novo = leitura.Leitura(nota=nota, status=status, resenha=resenha, livro=livro, usuario = usuario)
            leitura_service.save(leitura_novo)
            return redirect('leituras')

    return render(request, 'leituras/form.html', {
        'form': form,
        'livros': livros
    })

@login_required
def editar_leitura(request, id):
    leitura_bd = leitura_service.getById(id)
    if leitura_bd.usuario != request.user:
        return HttpResponse('Você não tem permissão para acessar essa página')

    livros = livro_service.getAll()
    form = LeituraForm(request.POST or None, instance=leitura_bd)

    if request.method == "POST":
        if form.is_valid():
            nota = request.POST.get('rating')
            livro = form.cleaned_data['livro']
            resenha = form.cleaned_data['resenha']
            status = form.cleaned_data['status']
            usuario = request.user
            leitura_novo = leitura.Leitura(nota=nota, status=status, resenha=resenha, livro=livro, usuario=usuario)
            leitura_service.update(leitura_bd, leitura_novo)
            return redirect('leituras')

    return render(request, 'leituras/form.html', {
        'edit': True,
        'form': form,
        'livros': livros
    })

@login_required
def visualizar_leitura(request, id):
    leitura_bd = leitura_service.getById(id)
    if leitura_bd.usuario != request.user:
        return HttpResponse('Você não tem permissão para acessar essa página')
    return render(request, 'leituras/view.html', {'leitura': leitura_bd})

@login_required
def deletar_leitura(request, id):
    leitura_bd = leitura_service.getById(id)

    if leitura_bd.usuario != request.user:
        return HttpResponse('Você não tem permissão para acessar essa página')

    if request.method == "POST":
        leitura_service.delete(leitura_bd)
        return redirect('leituras')

    return render(request, 'leituras/delete.html', {'leitura': leitura_bd})

def login_usuario(request):
    if request.method == "POST":
        form_login = LoginForm(data=request.POST)

        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']

            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                if usuario.is_superuser:
                    return redirect('leituras')
                else:
                    return redirect('leituras')
            else:
                print('op')
                form_login = LoginForm(data=request.POST)
        else:
            print(form_login.errors)
            form_login = LoginForm(data=request.POST)
    else:
        form_login = LoginForm()

    return render(request, 'usuario/login.html', {'form': form_login})

def cadastro(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            usuario_novo = usuario.Usuario(nome=nome, email=email, password=password)
            usuario_bd = usuario_service.cadastrar_usuario(usuario_novo)
            login(request, usuario_bd)
            return redirect('leituras')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/register.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')
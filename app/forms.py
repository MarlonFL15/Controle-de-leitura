from django import forms
from .models import Leitura, Livro, Usuario
from django.contrib.auth.forms import AuthenticationForm

class LeituraForm(forms.ModelForm):
    livro = forms.ModelChoiceField(queryset=Livro.objects.all(), widget=forms.Select(attrs={'id':'selectLivro'}))
    resenha = forms.CharField(required=False, widget=forms.Textarea())
    class Meta:

        model = Leitura
        fields = ['livro', 'status', 'nota', 'resenha']

#Cria o model personalizado de usuário

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label="Confirmação de Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'}))

    nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = Usuario
        fields = ['email', 'nome']

    #Função para verificar se as senhas são iguais
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2  and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais')
        return password2

    #sobreescreevendo a função "save" para criptografar a senha
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        model = Usuario
        fields = ['username', 'password']
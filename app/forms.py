from django import forms
from .models import Leitura, Livro
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class LeituraForm(forms.ModelForm):
    livro = forms.ModelChoiceField(queryset=Livro.objects.all(), widget=forms.Select(attrs={'id':'selectLivro'}))
    resenha = forms.CharField(widget=forms.Textarea())
    class Meta:

        model = Leitura
        fields = ['livro', 'status', 'nota', 'resenha']
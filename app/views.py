from django.shortcuts import render

# Create your views here.
def leituras(request):
    return render(request, 'leituras/leituras.html')

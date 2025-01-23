from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Formulario
from .forms import FormularioForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'cadastro.html', {'form': FormularioForm(), 'success_message': 'Cadastro realizado com sucesso!'})
    else:
        form = FormularioForm()  #
    return render(request, 'cadastro.html', {'form': form})
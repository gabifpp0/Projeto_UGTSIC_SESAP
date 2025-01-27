import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Formulario
from .forms import FormularioForm
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return render(request, 'cadastro.html', {'form': FormularioForm(), 'success_message': 'Cadastro realizado com sucesso!'})
    else:
        form = FormularioForm()
    return render(request, 'cadastro.html', {'form': form})

def inscricoes(request):
    curriculos = Formulario.objects.all()
    return render(request, 'tabela.html' ,{'curriculos': curriculos})

def email(request):
    
    return HttpResponse('Olá')
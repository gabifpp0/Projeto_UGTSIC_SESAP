import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm
from django.template.loader import get_template  
from django.core.mail import EmailMessage 
from django.utils import timezone
from django.conf import settings
import socket

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sendmail_contact(formulario):
    data = { 
        'name': formulario.nome, 
        'email': formulario.email,
        'obs': formulario.obs,
        'cargo': formulario.cargo,
        'telefone': formulario.telefone,
        'escolaridade': formulario.get_escolaridade_display(),
    }
    
    message_body = get_template('email.html').render(data)  
    
    sendmail = EmailMessage(
        'Novo Currículo Cadastrado',
        message_body, 
        settings.DEFAULT_FROM_EMAIL,
        to=[formulario.email] 
    )
    sendmail.content_subtype = "html"    
    return sendmail.send()

def cadastro(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            
            formulario = form.save(commit=False)
            formulario.ip = request.META.get('REMOTE_ADDR')
            formulario.dh = timezone.now()
            formulario.save()

            sendmail_contact(formulario)

            if sendmail_contact(formulario):
                return redirect('email')
            else:
                return render(request, 'cadastro.html', {'form': FormularioForm(), 'error_message': 'Cadastro realizado, mas houve um erro ao enviar o e-mail.'})
            
    else:
        form = FormularioForm()
    return render(request, 'cadastro.html', {'form': form})

def inscricoes(request):
    curriculos = Formulario.objects.all()
    return render(request, 'tabela.html' ,{'curriculos': curriculos})

def email(request):
    return render(request, 'email.html')
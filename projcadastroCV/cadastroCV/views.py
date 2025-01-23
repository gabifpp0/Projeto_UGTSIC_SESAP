from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Formulario

# Create your views here.

def index(request):
    formulario = Formulario.objects.all()
    context = {'formulario': formulario}
    return render(request, 'cadastro.html', context)
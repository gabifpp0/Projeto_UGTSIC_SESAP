from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Formulario(models.Model):
    ops_escolaridade = [
        "Ensino médio incompleto",
        "Ensino médio completo",
        "Ensino superior incompleto",
        "Ensino superior completo"
    ]
    
    nome = models.CharField(max_length=15,verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20,verbose_name="Telefone")
    cargo = models.CharField(max_length=100, verbose_name="Cargo desejado")
    escolaridade = models.CharField(max_length=25, choices=ops_escolaridade)
    obs = models.CharField(max_length=150, verbose_name="Observações")
    arquivo = models.FileField(upload_to='uploads/')

    def tamanho_arquivo(file):
        max_tamanho = 1
        if file.size > max_tamanho * 1024 * 1024:
            raise ValidationError("O arquivo excede o tamanho esperado")

    def __str__(self):
        return self.nome
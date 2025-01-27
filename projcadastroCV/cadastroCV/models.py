from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Formulario(models.Model):
    ops_escolaridade = [
        ("ensino_medio_incompleto","Ensino médio incompleto"),
        ("ensino_medio_completo","Ensino médio completo"),
        ("ensino_superior_incompleto","Ensino superior incompleto"),
        ("ensino_superior_completo","Ensino superior completo"),
    ]
    
    nome = models.CharField(max_length=15,verbose_name="Nome",blank=False)
    email = models.EmailField(verbose_name="E-mail", blank=False)
    telefone = models.CharField(max_length=11,verbose_name="Telefone", blank=False)
    cargo = models.CharField(max_length=100, verbose_name="Cargo desejado",blank=False)
    escolaridade = models.CharField(max_length=50,choices=ops_escolaridade, blank=False)
    obs = models.CharField(max_length=150, verbose_name="Observações", blank=True)
    arquivo = models.FileField(upload_to='uploads/', blank=False)
    ip = models.GenericIPAddressField(verbose_name="IP do Usuário", blank=True, null=True)
    dh = models.DateTimeField(verbose_name="Data e Hora do Envio", default=timezone.now)

    def __str__(self):
        return self.nome
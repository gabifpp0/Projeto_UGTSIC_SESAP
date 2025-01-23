from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'email', 'telefone', 'cargo', 'escolaridade', 'obs', 'arquivo']
        widgets = {
            'escolaridade': forms.Select(choices=Formulario.ops_escolaridade),
        }

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo', False)
        if arquivo:
            if arquivo.size > 1 * 1024 * 1024:
                raise forms.ValidationError('O arquivo excede o tamanho esperado - 1MB')
            return arquivo 
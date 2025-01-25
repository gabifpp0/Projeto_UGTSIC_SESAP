from django import forms
from .models import Formulario
import re

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'email', 'telefone', 'cargo', 'escolaridade', 'obs', 'arquivo']
        widgets = {
            'escolaridade': forms.Select(choices=Formulario.ops_escolaridade),
        }

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo', False)
        
        try:
            if arquivo:
                if arquivo.size > 1 * 1024 * 1024:
                    raise forms.ValidationError('O arquivo excede o tamanho esperado - 1MB')
            
                valido = ('.docx', '.doc', '.pdf')
                if not arquivo.name.lower.endswith(valido):
                    raise forms.ValidationError('Apenas arquivos doc, docx são permitidos')
            
            return arquivo
        except AttributeError:
            raise forms.ValidationError('Só são aceitos os formatos doc, docx ou pdf.')
        except Exception as e:
            raise forms.ValidationError('Erro ao validar')
        
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        
        try:
            numeros = re.sub(r'\D', '', telefone)

            if len(numeros) < 11:
                raise forms.ValidationError('O número de telefone deve ter pelo menos 11 dígitos (com DDD)')
            return telefone
        
        except AttributeError:
            raise forms.ValidationError("Telefone deve ser fornecido.")
        except re.error as e:
            raise forms.ValidationError(f"Erro na validação do formato do telefone: {str(e)}")
        except Exception as e:
            raise forms.ValidationError(f"{str(e)}")
 
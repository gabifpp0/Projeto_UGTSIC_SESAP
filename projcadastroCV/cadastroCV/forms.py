from django import forms
from .models import Formulario
import re, os

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
                # Verificar o tamanho do arquivo
                if arquivo.size > 1 * 1024 * 1024:
                    raise forms.ValidationError('O arquivo excede o tamanho esperado - 1MB')
                
                # Verificar a extensão do arquivo
                ext = os.path.splitext(arquivo.name)[1]
                valid_extensions = ['.docx', '.doc', '.pdf']
                if not ext.lower() in valid_extensions:
                    raise forms.ValidationError('Apenas arquivos doc, docx ou pdf são permitidos')
            return arquivo
        except AttributeError:
            raise forms.ValidationError('Nenhum arquivo foi enviado ou o arquivo é inválido.')
        except Exception as e:
            raise forms.ValidationError(f'Erro ao validar o arquivo: {str(e)}')
        
    #Validação telefone
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

class EmailForm(forms.Form):
    email = forms.EmailField()
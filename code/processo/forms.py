from django import forms
from django.forms import ModelForm
from processo.models import ProcessosAnexos, ProcessosHonorarios

class LawsuitFileForm(ModelForm):
    class Meta:
        model = ProcessosAnexos
        fields = "__all__"
        exclude = ["processo"]

        widgets = {
            'nome_do_anexo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'custom-file'}),
        }

class LawsuitValuesForm(ModelForm):
    class Meta:
        model = ProcessosHonorarios
        fields = "__all__"
        exclude = ["processo", "ganho"]

        widgets = {
            'referente': forms.TextInput(attrs={'class': 'form-control'}),
            'advogado_responsavel': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control money'}),

        }



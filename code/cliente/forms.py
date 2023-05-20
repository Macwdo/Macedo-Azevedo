from django import forms
from cliente.models import Cliente

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
        }
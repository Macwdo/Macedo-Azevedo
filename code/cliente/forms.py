from django import forms
from cliente.models import Cliente, ClienteContato, ClienteEndereco

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
            'image': forms.FileInput(attrs={'class': 'custom-file'})
        }


class ClientContactForm(forms.ModelForm):
    class Meta:
        model = ClienteContato
        fields = "__all__"

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClientAddressForm(forms.ModelForm):
    class Meta:
        model = ClienteEndereco
        fields = "__all__"

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from parte_adversa.models import AdversePart, AdversePartAddress, AdversePartContact

class AdversePartForm(forms.ModelForm):

    field_order = ['nome', 'tipo', 'cpf_cnpj', 'estado_civil', 'profissao', 'image']

    class Meta:
        model = AdversePart
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control type_select'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
        }


class AdversePartContactForm(forms.ModelForm):
    class Meta:
        model = AdversePartContact
        fields = "__all__"

        widgets = {
            'parte_adv': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control phone'}),
        }


class AdversePartAddressForm(forms.ModelForm):
    class Meta:
        model = AdversePartAddress
        fields = "__all__"

        widgets = {
            'parte_adv': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
        }

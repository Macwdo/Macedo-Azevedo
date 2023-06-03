from django import forms
from registry.models import Registry, RegistryContact, RegistryAddress

class RegistryForm(forms.ModelForm):
    field_order = ['name', 'civil_state', 'profession','client_of', 'cnpj', 'cpf', 'image']

    class Meta:
        model = Registry
        fields = ['name', 'civil_state', 'profession', 'image', 'client_of']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_state': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'client_of': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
        }
    

class RegistryContactForm(forms.ModelForm):
    class Meta:
        model = RegistryContact
        fields = "__all__"

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control phone'}),
        }


class RegistryAddressForm(forms.ModelForm):
    class Meta:
        model = RegistryAddress
        fields = "__all__"

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control'}),
            'complement': forms.TextInput(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
        }

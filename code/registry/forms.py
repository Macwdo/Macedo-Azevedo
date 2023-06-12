from django import forms
from registry.models import Registry, RegistryContact, RegistryAddress

class RegistryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["civil_state"].label = "Estado civil"
        self.fields["profession"].label = "Profissão"
        self.fields["client_of"].label = "Cliente de"


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
    def __init__(self, *args, **kwargs):
        super(RegistryContactForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["phone_number"].label = "Celular"

    class Meta:
        model = RegistryContact
        fields = "__all__"

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control phone'}),
        }


class RegistryAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryAddressForm, self).__init__(*args, **kwargs)
        self.fields["address"].label = "Endereço"
        self.fields["address_number"].label = "Número"
        self.fields["complement"].label = "Complemento"
        self.fields["reference"].label = "Referência"

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

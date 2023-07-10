from django import forms
from registry.models import Registry, RegistryCnpj, RegistryContact, RegistryAddress, RegistryCpf

class RegistryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["client_of"].label = "Cliente de"
        for k, v in self.fields.items():
            if self.fields[k].required == False:
                self.fields[k].label += " *"

    field_order = ['name', 'client_of', 'image']

    class Meta:
        model = Registry
        fields = ['name', 'image', 'client_of']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_of': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
        }
    

class RegistryContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryContactForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["phone_number"].label = "Celular"
        for k, v in self.fields.items():
            self.fields[k].required = False
            self.fields[k].label += " *"

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
        for k, v in self.fields.items():
            if self.fields[k].required == False:
                self.fields[k].label += " *"

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

class RegistryCpfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryCpfForm, self).__init__(*args, **kwargs)
        self.fields["cpf"].label = "CPF"
        self.fields["profession"].label = "Profissão"
        self.fields["civil_state"].label = "Estado Civil"
        for k, v in self.fields.items():
            self.fields[k].required = False

    class Meta:
        model = RegistryCpf
        fields = ["cpf", "profession", "civil_state"]
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_state': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistryCnpjForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistryCnpjForm, self).__init__(*args, **kwargs)
        self.fields["cnpj"].label = "CNPJ"
        self.fields["interprise_type"].label = "Ramo da empresa"
        for k, v in self.fields.items():
            self.fields[k].required = False
            
    class Meta:
        model = RegistryCnpj
        fields = ["cnpj", "interprise_type"]
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control cnpj'}),
            'interprise_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

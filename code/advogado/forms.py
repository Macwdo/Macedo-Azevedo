from django import forms

from advogado.models import Advogado
from user.models import MAUser
from django.core.exceptions import ValidationError


class LawyerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LawyerForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["email"].label = "Email do advogado"
        self.fields["user"].label = "Usuário"
        for k, v in self.fields.items():
            if self.fields[k].required == False:
                self.fields[k].label += " *"

    class Meta:
        model = Advogado
        fields = ['name', 'email', 'user', 'oab', 'cpf', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf', 'name': 'cpf'}),
            'oab': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'})
        }
        
        help_texts = {
            "email": "Esse email será usado para comunicação com clientes. Já o do usuário é para o uso dentro da plataforma." 
        }

        
    
    def clean_user(self):
        data: MAUser = self.cleaned_data["user"]
        if data is None:
            raise ValidationError("Indique um usuário para o Advogado")
        if data.username == "admin":
            raise ValidationError("Não é possível o Advogado pertencer ao usuário admin")
        try:
            lawyer = Advogado.objects.exists(user=data)
            if lawyer:
                raise ValidationError("Já existe um advogado aliado a esse usuário")
        except:
            return data

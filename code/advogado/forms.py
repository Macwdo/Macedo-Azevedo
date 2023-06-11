from django import forms

from advogado.models import Advogado


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ['name', 'email', 'oab', 'cpf', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf', 'name': 'cpf'}),
            'oab': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'})
        }

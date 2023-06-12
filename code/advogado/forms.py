from django import forms

from advogado.models import Advogado


class LawyerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LawyerForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"

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

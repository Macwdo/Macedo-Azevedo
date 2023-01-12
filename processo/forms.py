from django import forms

from .models import Processos


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processos
        fields = '__all__'
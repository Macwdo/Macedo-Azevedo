from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from registry.models import Registry, RegistryContact, RegistryAddress

class RegistryForm(forms.ModelForm):
    field_order = ['name', 'civil_state', 'profession', 'cnpj', 'cpf', 'image']

    class Meta:
        model = Registry
        fields = ['name', 'civil_state', 'profession', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_state': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
        }
    

class RegistryContactForm(forms.ModelForm):
    class Meta:
        model = RegistryContact
        fields = "__all__"

        widgets = {
            'registry': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control phone'}),
        }


class RegistryAddressForm(forms.ModelForm):
    class Meta:
        model = RegistryAddress
        fields = "__all__"

        widgets = {
            'registry': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control'}),
            'complement': forms.TextInput(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
        }

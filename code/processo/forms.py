from django import forms
from django.forms import ModelForm
from processo.models import ProcessosAnexos, ProcessosHonorarios, Processos
from django.core.exceptions import ValidationError


class LawsuitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LawsuitForm, self).__init__(*args, **kwargs)
        self.fields["finalizado"].required = False
        self.fields["observacoes"].required = False

    iniciado = forms.DateField(widget=forms.DateInput(attrs=
        {
            'class': 'form-control',
            'data-inputmask-alias': "datetime",
            'data-inputmask-inputformat': "dd/mm/yyyy",
            'data-mask': 'data-mask',
            'datepicker': 'datepicker',
        }
    ), label='Data de início')
    
    finalizado = forms.DateField(widget=forms.DateInput(attrs=
        {
            'class': 'form-control',
            'data-inputmask-alias': "datetime",
            'data-inputmask-inputformat': "dd/mm/yyyy",
            'data-mask': 'data-mask',
            'datepicker': 'datepicker',
        }
    ), label='Data de Fim')

    field_order = [
            'codigo_processo',
            'advogado_responsavel',
            'parte_adversa',
            'cliente',
            'cliente_de',
            'posicao',
            'colaborador',
            'assunto',
            'vara',
            'estado',
            'municipio',
            'observacoes',
            'iniciado',
            'finalizado',
        ]
    class Meta:
        model = Processos
        fields = "__all__"
        requireds = {
            'finalizado': False
        }
        widgets = {
            'codigo_processo': forms.TextInput(attrs={
                'class': 'form-control lawsuitcode-mask',
                'placeholder': 'NNNNNNN-DD.AAAA.J.TR.OOOO'
            }),
            'advogado_responsavel': forms.Select(attrs={'class': 'form-control select2bs4', 'style': 'width: 100%;'}),
            'parte_adversa': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'cliente': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'indicado_por': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'posicao': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'colaborador': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
            'vara': forms.TextInput(attrs={'class': 'form-control'}),
            'iniciado': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'finalizado': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control'})
        }
        
        

        help_texts = {
            'codigo_processo': 'Insira o codigo do processo.',
            'advogado_responsavel': 'Indique o Advogado do caso.',
            'parte_adversa': 'Indique a Parte adversa do caso.',
            'cliente': 'Indique o Cliente do caso',
            'cliente_de': 'Indique de qual advogado é o cliente.',
            'posicao': 'Indique a posição do cliente se ele vai ser autor ou réu no caso.',
            'colaborador': 'Indique caso exista algum colaborador no caso. (Campo opcional).',
            'observacoes': 'Caso exista alguma observação a ser feita, indique ela aqui é para escrever o que quiser.',
            'vara': 'Vara ou Cormarca do processo',
            'inicializado': 'Dia em que se iniciou o processo',
            'finalizado': 'Dia em que se finalizou o processo (Caso estiver em andamento deixar em branco).',
            'assunto': 'Indique o assunto do processo'
        }
        
    def clean_colaborador(self):
        data = self.cleaned_data['colaborador']
        if self.cleaned_data['colaborador'] == self.cleaned_data['advogado_responsavel']:
            raise ValidationError("O colaborador não pode ser o advogado do caso.")
        return data

    def clean_cliente(self):
        data = self.cleaned_data['cliente']
        if self.cleaned_data['cliente'] == self.cleaned_data['parte_adversa']:
            raise ValidationError("O Cliente não pode ser a parte adversa")
        return data


class LawsuitFileForm(ModelForm):
    class Meta:
        model = ProcessosAnexos
        fields = "__all__"
        exclude = ["processo"]

        widgets = {
            'nome_do_anexo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'custom-file'}),
        }


class LawsuitValuesForm(ModelForm):
    class Meta:
        model = ProcessosHonorarios
        fields = "__all__"
        exclude = ["processo", "ganho"]

        widgets = {
            'referente': forms.TextInput(attrs={'class': 'form-control'}),
            'advogado_responsavel': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'valor': forms.TextInput(attrs={'class': 'form-control money'}),

        }



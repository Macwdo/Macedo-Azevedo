from django.db import models

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV


def dir_files_processo(instance, file):
    clienteName = instance.cliente.nome.title().split()
    clienteName = "_".join(clienteName)
    parteAdvName = instance.parte_adversa.nome.title().split()
    parteAdvName = "_".join(parteAdvName)
    return f"{clienteName}X{instance.parte_adversa.nome}.png"


class Processos(models.Model):
    
    assunto_choices = [
        ("Trabalhista", "Direito Trabalhista"),
        ("Previdenciário", "Direito Previdenciário"),
        ("Civil", "Direito Civil")
    ]

    posicao_choice = [
        ("Autor", "Autor"),
        ("Réu", "Réu")
    ]

    codigo_processo = models.CharField(max_length=25, unique=True)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, related_name="advogado_responsavel", default="Não Informado")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="clientes")
    cliente_de = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null= True, blank=False)
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    assunto = models.CharField(choices=assunto_choices, max_length=15)
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    honorarios = models.FloatField(blank=True, default=0)
    municipio = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    n_vara = models.CharField(max_length=30)
    vara = models.CharField(max_length=50)
    iniciado = models.DateTimeField(auto_now_add=True)
    finalizado = models.DateTimeField(blank=True, null=True)
    anexo = models.ImageField(upload_to=dir_files_processo, default=None, null=True, blank=True)

    def __str__(self) -> str:
        clienteName = self.cliente.nome.title().split()
        parteAdvName = self.parte_adversa.nome.title().split()
        clienteName = "_".join(clienteName)
        parteAdvName = "_".join(parteAdvName)
        return f"{clienteName}X{parteAdvName}_{self.codigo_processo}"


    class Meta:
        verbose_name_plural = 'Processos'



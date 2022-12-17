from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
import os
from .models import Processos, ProcessosArquivos

def delete_empty_folders(path):
    root = path
    folders = list(os.walk(root))[1:]
    for folder in folders:
        if not folder[2]:
            os.rmdir(folder[0])


def delete_file(instance, **kwargs):
    many = kwargs.get("many", None)
    if many:
        try:
            os.remove(instance.arquivos.path)
            delete_empty_folders("./files")
        except(ValueError, FileNotFoundError):
            print("Error")
    else:
        try:
            os.remove(instance.arquivo.path)
            delete_empty_folders("./files")
        except(ValueError, FileNotFoundError):
            print("Error")



@receiver(pre_delete, sender=ProcessosArquivos)
def processoArquivos_delete(sender, instance, *args, **kwargs):
    old_instance = ProcessosArquivos.objects.get(pk=instance.pk)
    delete_file(old_instance)

@receiver(pre_delete, sender=Processos)
def processo_delete(sender, instance, *args, **kwargs):
    old_instance = Processos.objects.get(pk=instance.pk)
    delete_file(old_instance, many=True)







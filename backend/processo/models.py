from django.db import models

# Create your models here.
def create_dir(instance,file):
    
    return f"{instance.nome}/{file}"

class ArquivoModels(models.Model):
    nome = models.CharField(max_length=20, default="Nada")
    files = models.FileField(upload_to=create_dir)

    def str(self):
        return f"{self.files}"

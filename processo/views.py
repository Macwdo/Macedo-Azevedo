from rest_framework.viewsets import ModelViewSet
from .models import Processos, ProcessosArquivos
from .serializers import ProcessosSerializer, ProcessosArquivosSerializer


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer


class ProcessosArquivosViewSet(ModelViewSet):
    queryset = ProcessosArquivos.objects.all()
    serializer_class = ProcessosArquivosSerializer

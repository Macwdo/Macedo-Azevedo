from rest_framework.viewsets import ModelViewSet
from .models import Processos, ProcessosArquivos
from .serializers import ProcessosSerializer, ProcessosArquivosSerializer
from rest_framework.permissions import IsAuthenticated

class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = []


class ProcessosArquivosViewSet(ModelViewSet):
    queryset = ProcessosArquivos.objects.all()
    serializer_class = ProcessosArquivosSerializer



    

    


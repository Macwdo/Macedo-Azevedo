from rest_framework.viewsets import ModelViewSet
from .models import Processos, ProcessosArquivos
from .serializers import ProcessosSerializer, ProcessosArquivosSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView

class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]


class ProcessosArquivosViewSet(ModelViewSet):
    queryset = ProcessosArquivos.objects.all()
    serializer_class = ProcessosArquivosSerializer
    permission_classes = [IsAuthenticated]

class renderPage(TemplateView):
    template_name = "index.html"
    

    


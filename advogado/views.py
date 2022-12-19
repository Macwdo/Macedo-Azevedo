from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Advogado
from .serializer import AdvogadoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AdvogadoViewSet(ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    permission_classes = [IsAuthenticated]
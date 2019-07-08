from django.shortcuts import render
from rest_framework import viewsets
from .models import PlanoComissoes
from .serializers import PlanosSerializer

# Create your views here.
class PlanosViewSet(viewsets.ModelViewSet):
    queryset = PlanoComissoes.objects.all()
    serializer_class = PlanosSerializer
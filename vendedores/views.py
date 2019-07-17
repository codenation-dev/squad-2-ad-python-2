from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendedor
from .serializers import VendedoresSerializer

# Create your views here.


class VendedoresViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedoresSerializer


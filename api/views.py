from rest_framework import viewsets
from .models import Encargado, Recurso, TipoRecurso, TipoEncargado, Proveedor
from .serializers import EncargadoSerializer, RecursoSerializer, TipoRecursoSerializer, TipoEncargadoSerializer, \
    ProveedorSerializer

from django_filters import rest_framework as filters


class EncargadoFilter(filters.FilterSet):
    class Meta:
        model = Encargado
        fields = {
            'nombre': ['icontains'],
            'telefono': ['icontains']
        }


class RecursoFilter(filters.FilterSet):
    class Meta:
        model = Recurso
        fields = {
            'serial': ['iexact'],
            'marca': ['iexact'],
        }


class EncargadoView(viewsets.ModelViewSet):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer
    filterset_class = EncargadoFilter


class RecursoView(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filterset_class = RecursoFilter


class TipoRecursoView(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer


class TipoEncargadoView(viewsets.ModelViewSet):
    queryset = TipoEncargado.objects.all()
    serializer_class = TipoEncargadoSerializer


class ProveedorView(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

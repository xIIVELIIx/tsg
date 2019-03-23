from .models import Encargado, Recurso, TipoRecurso, TipoEncargado, Proveedor
from rest_framework import serializers


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = ('id', 'nombre', 'telefono', 'tipo')


class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('id', 'serial', 'tipo', 'proveedor', 'estado', 'encargado', 'fechaAsignacion', 'marca')


class TipoEncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEncargado
        fields = ('id', 'descripcion')


class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = ('id', 'descripcion')


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre')

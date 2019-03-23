from django.db import models


class TipoEncargado(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class TipoRecurso(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class Encargado(models.Model):
    nombre = models.CharField(max_length=60)
    telefono = models.BigIntegerField()
    tipo = models.ForeignKey(TipoEncargado, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
    serial = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoRecurso, null=True, blank=True, on_delete=models.SET_NULL)
    marca = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.SET_NULL)
    fechaCompra = models.DateField(auto_now=True)
    estado = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    encargado = models.ForeignKey(Encargado, null=True, blank=True, on_delete=models.SET_NULL)
    fechaAsignacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.descripcion

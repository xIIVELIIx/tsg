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
    tipo = models.ForeignKey(TipoEncargado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
    serial = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fechaCompra = models.DateField(auto_now=True)
    estado = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    fechaAsignacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.descripcion

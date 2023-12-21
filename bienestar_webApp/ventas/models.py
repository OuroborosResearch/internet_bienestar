from django.conf import settings
from django.db import models
from django.utils import timezone


class Venta(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    calle = models.CharField(max_length=50)
    no_ext = models.IntegerField()
    no_int = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    referencias = models.TextField()
    created_date = models.DateTimeField(
            auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        # Ordenar de más nuevos a más viejo

    def __str__(self):
        return str(self.nombre)
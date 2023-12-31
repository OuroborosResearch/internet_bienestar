from django.conf import settings
from django.db import models
from django.utils import timezone


class Venta(models.Model):
    PLANES_CHOICES = (
        (100, 'Obten tu Chip'),
        (50, 'Paquete 50'),
        (65, 'Paquete 65'),
        (100, 'Paquete 100'),
        (125, 'Paquete 125'),
        (200, 'Paquete 200'),
    )
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    calle = models.CharField(max_length=50)
    no_ext = models.CharField(max_length=50)
    no_int = models.CharField(max_length=10,blank=True, null=True)
    colonia = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    referencias = models.TextField()
    precio = models.IntegerField(choices=PLANES_CHOICES)
    cantidad = models.IntegerField()
    created_date = models.DateTimeField(
            auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        # Ordenar de más nuevos a más viejo

    def __str__(self):
        return str(self.nombre)
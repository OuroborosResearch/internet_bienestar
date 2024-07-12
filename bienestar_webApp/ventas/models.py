from django.conf import settings
from django.db import models
from django.utils import timezone


class ChipOffers(models.Model):
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    mp_link = models.CharField(max_length=900, null=True, blank=True)
    precio = models.IntegerField(verbose_name="Precio")
    envio_gratuito = models.BooleanField()
    created_date = models.DateTimeField(
            auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Oferta chip'
        verbose_name_plural = 'Ofertas Chip'
        # Ordenar de más nuevos a más viejo

    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    PLANES_CHOICES = (
        (100, 'Obten tu Chip'),
        (50, 'Paquete 50'),
        (60, 'Paquete 60'),
        (99, 'Paquete 99'),
        (100, 'Paquete 100'),
        (120, 'Paquete 120'),
        (200, 'Paquete 200'),
        (230, 'Paquete 230'),
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
    aceptar_aviso = models.BooleanField(default=False)
    aceptar_terminos = models.BooleanField(default=False)
    created_date = models.DateTimeField(
            auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        # Ordenar de más nuevos a más viejo

    def __str__(self):
        return str(self.nombre)
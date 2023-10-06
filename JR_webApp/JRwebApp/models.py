from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


# Create your models here.
class Paginas(models.Model):
    titulo = models.CharField(
        verbose_name="Título",
        max_length=200)
    contenido = RichTextField(
        verbose_name="Contenido",blank=True, null=True)
    imagen = models.ImageField(
        upload_to="pags/JRwebApp/terminos", 
        blank=True, null=True, 
    )
    pdf = models.FileField(
        upload_to="pags/JRwebApp/pdfs",
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Páginas'
        verbose_name_plural = 'Páginas'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.titulo

class Planes(models.Model):
    titulo = models.CharField(
        verbose_name="Título",
        max_length=200)
    contenido = models.TextField(
        verbose_name="Contenido",blank=True, null=True)
    imagen = models.ImageField(
        upload_to="JRwebApp/planes", 
        blank=True, null=True, 
    )

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Planes'
        verbose_name_plural = 'Planes'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.titulo
    
class Reviews(models.Model):
    titulo = models.CharField(
        verbose_name="Título",
        max_length=200)
    contenido = models.TextField(
        verbose_name="Contenido",blank=True, null=True)
    imagen = models.ImageField(
        upload_to="terminos", 
        blank=True, null=True, 
    )

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.titulo
    
class Blog(models.Model):


    titulo = models.CharField(
        verbose_name="Título",
        max_length=200)
    contenido = models.TextField(
        verbose_name="Contenido",blank=True, null=True)
    imagen = models.ImageField(
        upload_to="terminos", 
        blank=True, null=True, 
    )

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.titulo
    

class Faqs (models.Model):
    pregunta = models.CharField(
        verbose_name="Pregunta",
        max_length=250)
    respuesta = RichTextField(
        verbose_name="Respuesta",blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'FAQS'
        verbose_name_plural = 'FAQS'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return str(self.pk)
    

class Aviso (models.Model):
    titulo = models.CharField(
        verbose_name="Título",
        max_length=250)
    contenido = RichTextField(
        verbose_name="Contenido",blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Aviso de Privacidad'
        verbose_name_plural = 'Aviso de Privacidad'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return str(self.pk)
    
    

class Entradas(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              limit_choices_to={'is_staff': True})
    etiquetas = models.ManyToManyField('Etiquetas')
    imagen = models.ImageField(
        upload_to="Imagen de portada", 
        blank=True, null=True, 
    )
    contenido = RichTextField(
        verbose_name="Contenido",blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Entradas Blog'
        verbose_name_plural = 'Entradas Blog'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.titulo
    

class Etiquetas(models.Model):
    name = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Etiquetas Blog'
        verbose_name_plural = 'Etiquetas Blog'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return str(self.name)


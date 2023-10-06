from django.contrib import admin
from .models import Paginas, Reviews, Entradas, Faqs, Etiquetas, Planes, Aviso
# Register your models here.
class PaginasAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'titulo','contenido',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Paginas, PaginasAdmin)

class ReviewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'titulo','contenido',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Reviews, ReviewsAdmin)


class FaqsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'pregunta','respuesta',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Faqs, FaqsAdmin)

class EntradasAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'titulo','autor',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Entradas, EntradasAdmin)

class EtiquetasAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'pk','name',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Etiquetas, EtiquetasAdmin)

class PlanesAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'pk','titulo',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Planes, PlanesAdmin)

class AvisoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'pk','titulo',
        )
    readonly_fields = ('created', 'updated')

admin.site.register(Aviso, AvisoAdmin)
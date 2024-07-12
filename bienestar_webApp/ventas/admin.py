from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Venta, ChipOffers

class VentasAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'nombre', 'celular', 'email'
    )
    readonly_fields = ('created_date',)

admin.site.register(Venta, VentasAdmin)

class ChipOffersAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'nombre',
    )
    readonly_fields = ('created_date',)

admin.site.register(ChipOffers, ChipOffersAdmin)

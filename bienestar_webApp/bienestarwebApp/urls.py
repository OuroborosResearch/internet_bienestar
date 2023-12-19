from django.urls import path, include
from . import views as landing_views

urlpatterns = [
    # Index admin
    path('', landing_views.intro, name="intro"),
    path('pags/<str:page_name>', landing_views.paginas, name="pags"),
    path('recargas', landing_views.mercado_pago_api, name="recargas"),
    path('consultas', landing_views.consultas, name="consultas"),
    path('nuevodistribuidor', landing_views.distribuidores, name="distribuidores"),
    path('aviso_privacidad', landing_views.avisos_privacidad, name="aviso_privacidad"),
    path('faqs', landing_views.faqs, name="faqs"),
    path('contact', landing_views.contact, name="contact"),
    path('about', landing_views.about, name="about"),
    path('cobertura', landing_views.cobertura, name="cobertura"),
    path('hbb', landing_views.hbb, name="hbb"),
    path('map/', landing_views.maps_view, name="maps_view"),
    path('autocomplete/', landing_views.autocomplete, name="autocomplete"),
    path('hbb_result/ok', landing_views.hbb_result_ok, name="hbb_result_ok"),
    path('hbb_result/', landing_views.hbb_result_fail, name="hbb_result_fail"),
    path('redireccionar/', landing_views.redireccion_recarga, name='redireccion_recarga'),
    path('compra_tu_chip_ib/', landing_views.compraChip, name='compra_tu_chip_ib'),
]
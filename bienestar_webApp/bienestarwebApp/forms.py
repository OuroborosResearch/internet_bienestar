from django import forms
from django.forms import NumberInput, TextInput, EmailInput, HiddenInput, Textarea, ChoiceField, Select, CheckboxInput,BooleanField
from ventas.models import Venta
from django.db.models import Q

class VentasFormulario(forms.ModelForm):

    class Meta:
        model = Venta
        fields ="__all__"
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Nombre', 'class' : 'form-group', 'readonly': True}),
            'apellido': HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}),
            'email': TextInput(attrs={'placeholder': 'Correo Electronico', 'class': 'form-control'}),
            'celular': NumberInput(attrs={'placeholder': 'Telefono Celular', 'class': 'form-control'}),
            'calle': TextInput(attrs={'placeholder': 'Calle', 'class': 'form-control'}),
            'no_ext': TextInput(attrs={'placeholder': 'Numero Exterior', 'class': 'form-control'}),
            'no_int': TextInput(attrs={'placeholder': 'Numero Interior', 'class': 'form-control'}),
            'colonia': TextInput(attrs={'placeholder': 'Colonia', 'class': 'form-control'}),
            'codigo_postal': TextInput(attrs={'placeholder': 'C.P.', 'class': 'form-control'}),
            'estado': TextInput(attrs={'placeholder': 'Estado', 'class': 'form-control'}),
            'municipio': TextInput(attrs={'placeholder': 'Municipio', 'class': 'form-control'}),
            'referencias': Textarea(attrs={'placeholder': 'Referencia del domicilio', 'rows': 5,'cols':50,'style':'height: 300%', 'class': 'form-control'}),
            'precio': HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}),
            'cantidad': HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}),
            'aceptar_aviso': HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}), 
            'aceptar_terminos':HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}),
            'created_date': HiddenInput(
                attrs={
                    'required': False,
                    'readonly': True,
                    'hidden': True,
                }),
            'paquete': HiddenInput(attrs={'required': False,
                    'readonly': True,
                    'hidden': True}),
        }
        
class OfertasFormulario(forms.ModelForm):

    class Meta:
        model = Venta
        fields =('precio', 'nombre', 'email', 'aceptar_aviso', 'aceptar_terminos')
        widgets = {
            'precio': Select(choices=Venta.PLANES_CHOICES,attrs={'placeholder': 'Elige tu plan'}),
            'nombre': TextInput(attrs={'placeholder': 'Nombre completo', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Correo Electronico', 'class': 'form-control'}),
            'aceptar_aviso': CheckboxInput(attrs={'style':'margin-top: 5px;'}), 
            'aceptar_terminos':CheckboxInput(attrs={'style':'margin-top: 5px;'}),
        }

class ImeiForm(forms.Form):
    imei = forms.IntegerField()
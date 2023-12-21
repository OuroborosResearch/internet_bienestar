from django import forms
from django.forms import NumberInput, TextInput, EmailInput, HiddenInput, Textarea
from ventas.models import Venta

class VentasFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VentasFormulario, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = ''
    class Meta:
        model = Venta
        fields ="__all__"
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Nombre Completo'}),
            'email': TextInput(attrs={'placeholder': 'Correo Electronico'}),
            'celular': TextInput(attrs={'placeholder': 'Telefono Celular'}),
            'calle': TextInput(attrs={'placeholder': 'Calle'}),
            'no_ext': TextInput(attrs={'placeholder': 'Numero Exterior'}),
            'no_int': TextInput(attrs={'placeholder': 'Numero Interior'}),
            'colonia': TextInput(attrs={'placeholder': 'Colonia'}),
            'codigo_postal': TextInput(attrs={'placeholder': 'C.P.'}),
            'estado': TextInput(attrs={'placeholder': 'Estado'}),
            'municipio': TextInput(attrs={'placeholder': 'Municipio'}),
            'referencias': Textarea(attrs={'placeholder': 'Referencia del domicilio', 'rows': 5,'cols':50,'style':'height: 300%'}),
            'created_date': HiddenInput(
                attrs={
                    'required': False,
                    'readonly': True,
                    'hidden': True,
                })
        }
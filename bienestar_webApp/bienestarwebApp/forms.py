from django import forms
from django.forms import NumberInput, TextInput, EmailInput, HiddenInput, Textarea, ChoiceField, Select, CheckboxInput,BooleanField
from ventas.models import Venta
from django.db.models import Q

class VentasFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VentasFormulario, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'aceptar_aviso' and field != 'aceptar_terminos':
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].label = ''
            else:
                #self.fields[field].widget.attrs['class'] = 'form-check-input'
                self.fields[field].widget.attrs['style'] = 'display: flex;'

    class Meta:
        model = Venta
        fields ="__all__"
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': TextInput(attrs={'placeholder': 'Apellido'}),
            'email': TextInput(attrs={'placeholder': 'Correo Electronico'}),
            'celular': NumberInput(attrs={'placeholder': 'Telefono Celular'}),
            'calle': TextInput(attrs={'placeholder': 'Calle'}),
            'no_ext': TextInput(attrs={'placeholder': 'Numero Exterior'}),
            'no_int': TextInput(attrs={'placeholder': 'Numero Interior'}),
            'colonia': TextInput(attrs={'placeholder': 'Colonia'}),
            'codigo_postal': TextInput(attrs={'placeholder': 'C.P.'}),
            'estado': TextInput(attrs={'placeholder': 'Estado'}),
            'municipio': TextInput(attrs={'placeholder': 'Municipio'}),
            'referencias': Textarea(attrs={'placeholder': 'Referencia del domicilio', 'rows': 5,'cols':50,'style':'height: 300%'}),
            'precio': Select(choices=Venta.PLANES_CHOICES,attrs={'placeholder': 'Elige tu plan'}),
            'cantidad': NumberInput(attrs={'placeholder': 'Cantidad','max': '10','min':'1','value': '1'}),
            'aceptar_aviso': CheckboxInput(attrs={'style':'margin-top: 5px;'}), 
            'aceptar_terminos':CheckboxInput(attrs={'style':'margin-top: 5px;'}),
            'created_date': HiddenInput(
                attrs={
                    'required': False,
                    'readonly': True,
                    'hidden': True,
                })
        }

class ImeiForm(forms.Form):
    imei = forms.IntegerField()
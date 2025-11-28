from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    #rows define la cantidad de filas que se muestran en el textarea
    class Meta:
        model = Equipo
        fields = ['cliente', 'tipo', 'problema']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de equipo'}),
            'problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del problema'}),
        }
        labels = {
            'cliente': 'Nombre del Cliente',
            'tipo': 'Tipo de Equipo',
            'problema': 'Problema Informado',
        }

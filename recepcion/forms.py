from django import forms
from django.core.exceptions import ValidationError
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

    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente', '')
        if cliente is None:
            return cliente
        if len(cliente.strip()) < 3:
            raise ValidationError('El nombre del cliente debe tener al menos 3 caracteres.')
        return cliente.strip()

    def clean_problema(self):
        problema = self.cleaned_data.get('problema', '')
        if problema is None:
            return problema
        if len(problema.strip()) < 10:
            raise ValidationError('Describa el problema con al menos 10 caracteres.')
        return problema.strip()

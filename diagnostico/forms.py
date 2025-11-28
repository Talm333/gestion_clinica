from django import forms
from .models import Diagnostico, Estudiante, Asignacion
from recepcion.models import Equipo

class AsignacionForm(forms.ModelForm):
    # campo para nuevo estudiante
    nuevo_estudiante = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del nuevo estudiante (Opcional)'}), 
        label="O registrar Nuevo Estudiante"
    )

    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Seleccionar Estudiante Existente"
    )

    # equipos sin asignar
    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.filter(asignacion__isnull=True, diagnosticos__isnull=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Equipo a Asignar"
    )

    class Meta:
        model = Asignacion
        fields = ['equipo', 'estudiante', 'nuevo_estudiante']

class SeleccionEquipoForm(forms.Form):
    # formulario solo para seleccionar qué equipo evaluar
    equipo = forms.ModelChoiceField(
        # equipos que tienen asignacion pero no tienen diagnostico
        queryset=Equipo.objects.filter(asignacion__isnull=False, diagnosticos__isnull=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Seleccionar Equipo Asignado para Diagnosticar"
    )

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['diagnostico', 'solucion', 'tipo_solucion']
        widgets = {
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalle del diagnóstico'}),
            'solucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Solución propuesta'}),
            'tipo_solucion': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'diagnostico': 'Diagnóstico Técnico',
            'solucion': 'Solución Recomendada',
            'tipo_solucion': 'Tipo de Solución',
        }

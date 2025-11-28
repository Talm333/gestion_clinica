from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        cleaned = super().clean()
        nuevo = cleaned.get('nuevo_estudiante')
        estudiante = cleaned.get('estudiante')

        if not nuevo and not estudiante:
            raise ValidationError('Debe seleccionar un estudiante existente o ingresar uno nuevo.')

        if nuevo:
            nuevo_nombre = nuevo.strip()
            if len(nuevo_nombre) < 3:
                self.add_error('nuevo_estudiante', 'El nombre del estudiante debe tener al menos 3 caracteres.')
            else:
                # crear o recuperar estudiante y asignarlo
                estudiante_obj, _ = Estudiante.objects.get_or_create(nombre=nuevo_nombre)
                cleaned['estudiante'] = estudiante_obj

        return cleaned

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

    def clean_diagnostico(self):
        diag = self.cleaned_data.get('diagnostico', '')
        if diag is None:
            return diag
        if len(diag.strip()) < 10:
            raise ValidationError('El diagnóstico debe contener al menos 10 caracteres.')
        return diag.strip()

    def clean_solucion(self):
        sol = self.cleaned_data.get('solucion', '')
        if sol is None:
            return sol
        if len(sol.strip()) < 10:
            raise ValidationError('La solución debe contener al menos 10 caracteres.')
        return sol.strip()

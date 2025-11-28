from django import forms
from .models import Entrega
from diagnostico.models import Diagnostico

class EntregaForm(forms.ModelForm):
    # Filtramos diagnosticos que NO tengan entrega asociada
    # esto es lo mismo que decir dame los diagnosticos que tengan null en entrega
    diagnostico = forms.ModelChoiceField(
        queryset=Diagnostico.objects.filter(entrega__isnull=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Diagnóstico a Entregar"
    )

    class Meta:
        model = Entrega
        fields = ['diagnostico']

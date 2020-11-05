from django import forms
from .models import Apartment
from django.forms import ModelForm

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'rate', 'capacity']
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "rate": "Tarifa",
            "capacity": "Capacidad"
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
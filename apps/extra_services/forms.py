from django import forms
from .models import ExtraService
from django.forms import ModelForm

class ExtraServiceForm(forms.ModelForm):
    class Meta:
        model = ExtraService
        fields = ['name', 'description', 'price', 'extra_service_category']
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "price": "Precio",
            "extra_service_category": "Categoría"
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
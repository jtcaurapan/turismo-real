from django import forms
from .models import Apartment
from .models import ApartmentImage



class ApartmentForm(forms.ModelForm):
    capacity = forms.ChoiceField(choices =  (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')))

    class Meta:
        model = Apartment
        fields = ['name', 'description', 'rate', 'capacity', 'address']
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "rate": "Tarifa",
            "capacity": "Capacidad",
            "address": "Dirección",
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }


class ApartmentImageForm(forms.ModelForm):
    class Meta:
        model = ApartmentImage
        fields = ['imageFile']
        labels = {
            "imageFile": "Imagen"
        }

        widgets = {
            'imageFile': forms.FileInput(),
        }


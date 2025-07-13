from django.forms import ModelForm
from .models import Inflow
from django import forms


class InflowForm(ModelForm):
    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        labels = {
            'supplier': 'Supplier',
            'product': 'Product',
            'quantity': 'Quantity',
            'description': 'Description',
        }
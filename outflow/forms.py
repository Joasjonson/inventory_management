from django.forms import ModelForm
from .models import Outflow
from django import forms


class OutflowForm(ModelForm):
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'product': 'Product',
            'quantity': 'Quantity',
            'description': 'Description',
        }


    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise forms.ValidationError(f"Quantity exceeds available stock. There are only {product.quantity} '{product.title}' in stock.")
        return quantity
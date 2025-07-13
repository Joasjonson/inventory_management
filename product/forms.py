from django.forms import ModelForm
from .models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price', 'quantity']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Product Title',
            'category': 'Category',
            'brand': 'Brand',
            'description': 'Description',
            'serie_number': 'Serie Number',
            'cost_price': 'Cost Price',
            'selling_price': 'Selling Price',
            'quantity': 'Quantity',
        }

    
    def clean_cost_price(self):
        cost_price = self.cleaned_data.get('cost_price')
        if cost_price < 0:
            raise forms.ValidationError("Cost price cannot be negative.")
        return cost_price

    def clean_selling_price(self):
        selling_price = self.cleaned_data.get('selling_price')
        if selling_price < 0:
            raise forms.ValidationError("Selling price cannot be negative.")
        return selling_price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity
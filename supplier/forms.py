from supplier.models import Supplier
from django import forms


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        labels = {
            'name': 'Supplier Name',
            'description': 'Description',
        }

        error_messages = {
            'name': {
                'required': 'Please enter a supplier name',
            },
            'description': {
                'required': 'Please enter a description',
            },
        }
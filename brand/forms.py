from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        labels = {
            'name': 'Brand Name',
            'description': 'Description',
        }

        error_messages = {
            'name': {
                'required': 'Please enter a brand name',
            },
            'description': {
                'required': 'Please enter a description',
            },
        }

      
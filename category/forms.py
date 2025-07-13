from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        labels = {
            'name': 'Category Name',
            'description': 'Description',
        }

        error_messages = {
            'name': {
                'required': 'Please enter a category name',
            },
            'description': {
                'required': 'Please enter a description',
            },
        }
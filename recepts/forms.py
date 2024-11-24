from django import forms
from django_select2 import forms as s2forms

from recepts.models import Recipe

class CategoryWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'name__icontains',
        'slug__icontains',
    ]

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['category', 'title', 'body']

        widgets = {
            'category': CategoryWidget, 
        }
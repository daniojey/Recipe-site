from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView

from recepts.forms import RecipeCreateForm

# Create your views here.

class HomePage(TemplateView):
    template_name = 'recepts/home.html'

class CreateRecipe(FormView):
    template_name = 'recepts/createrecipte.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes:home')

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        form.save()
        return super().form_valid(form)
    
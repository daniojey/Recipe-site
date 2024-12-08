from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView

from recepts.forms import RecipeCreateForm
from recepts.models import Recipe

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
    

class RecipesPageView(TemplateView):
    template_name = 'recepts/recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(Recipe.objects.all())

        context["recipes"] = Recipe.objects.all().select_related('category').order_by('-date_taken')
        return context
    
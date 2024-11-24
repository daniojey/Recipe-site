from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=205, verbose_name='Назва рецепту')
    body = models.CharField(max_length=3000, verbose_name='Рецепт')
    date_taken = models.DateTimeField(auto_now_add=True)
    
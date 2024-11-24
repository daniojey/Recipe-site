from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва')
    slug = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name='recipes', verbose_name='Категорія')
    title = models.CharField(max_length=205, verbose_name='Назва рецепту')
    body = models.CharField(max_length=3000, verbose_name='Рецепт')
    date_taken = models.DateTimeField(auto_now_add=True)

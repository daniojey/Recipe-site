from django.db import models

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва')
    slug = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Recipe(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name='recipes', verbose_name='Категорія')
    title = models.CharField(max_length=205, verbose_name='Назва рецепту')
    body = models.CharField(max_length=3000, verbose_name='Рецепт')
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Категорія - {self.category}, Автор - {self.author}, Название - {self.title}"

    class Meta:
        db_table = "recipes"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
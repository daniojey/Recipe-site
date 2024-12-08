from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    def __str__(self):
        return  self.username

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
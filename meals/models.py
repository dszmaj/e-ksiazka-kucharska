from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class MealCategory(models.Model): # adding only from admin panel
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class MealComment(models.Model):
    body = models.TextField("Treść", null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Meal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    recipe = models.TextField("Sposób przyrządzenia", null=True)
    category = models.ManyToManyField(MealCategory)
    photo = models.ImageField("Zdjęcie produktu", upload_to='images/%Y/%m/%d/', blank=True, null=True)
    PREPARATION_TIME_CHOICES = (
        ('very_fast', 'poniżej 15 minut'),
        ('fast', '15 - 30 minut'),
        ('medium', '30 - 60 minut'),
        ('long', 'powyżej 60 minut'),
    )
    preparation_time = models.CharField("Czas przygotowania",
                                        max_length=50, choices=PREPARATION_TIME_CHOICES, default='fast')

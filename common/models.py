from django.db import models
from products.models import Product
from meals.models import Meal


class Amounts(models.Model):
    value = models.PositiveIntegerField()
    meal = models.ForeignKey(Meal, related_name='amounts', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='amounts', on_delete=models.CASCADE)

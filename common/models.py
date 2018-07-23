from django.db import models
from products.models import Product
from meals.models import Meal


class Amounts(models.Model):
    value = models.PositiveIntegerField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

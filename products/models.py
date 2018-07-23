from django.contrib.auth.models import User
from django.db import models


class ProductCategory(models.Model):  # adding only from admin panel
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


class ProductComment(models.Model):
    body = models.TextField("Treść", null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Product(models.Model):
    name = models.CharField("Nazwa dania", max_length=150, null=True)
    kcal = models.PositiveIntegerField("Ilość kalorii w 100g", null=True)
    protein = models.DecimalField("Zawartość białka w 100g", max_digits=5, decimal_places=1, null=True)
    carbohydrate = models.DecimalField("Zawartość węglowodanów 100g", max_digits=5, decimal_places=1, null=True)
    sugar = models.DecimalField("Zawartość cukru w 100g", max_digits=5, decimal_places=1, null=True)
    fat = models.DecimalField("Zawartość tłuszczu w 100g", max_digits=5, decimal_places=1, null=True)
    fibre = models.DecimalField("Zawartość błonnika w 100g", max_digits=5, decimal_places=1, null=True)
    photo = models.ImageField("Zdjęcie produktu", upload_to='images/%Y/%m/%d/', blank=True, null=True)
    category = models.ManyToManyField(ProductCategory)
    comment = models.ForeignKey(ProductComment, on_delete=models.CASCADE)



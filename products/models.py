from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):  # adding only from admin panel
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Product name'), max_length=150)
    kcal = models.PositiveIntegerField(_('Calories per 100g'), null=True)
    protein = models.DecimalField(_('Protein per 100g'), max_digits=5, decimal_places=1, null=True)
    carbohydrate = models.DecimalField(_('Carbohydrate per 100g'), max_digits=5, decimal_places=1, null=True)
    sugar = models.DecimalField(_('Sugar per 100g'), max_digits=5, decimal_places=1, null=True)
    fat = models.DecimalField(_('Fat per 100g'), max_digits=5, decimal_places=1, null=True)
    fibre = models.DecimalField(_('Fibre per 100g'), max_digits=5, decimal_places=1, null=True)
    photo = models.ImageField(_('Photo'), upload_to='images/%Y/%m/%d/', blank=True, null=True)
    category = models.ManyToManyField(ProductCategory, related_name='products')

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    body = models.CharField(_('Content'), null=True, max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.product

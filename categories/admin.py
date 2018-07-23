from django.contrib import admin
from products.models import ProductCategory
from meals.models import MealCategory


admin.site.register(ProductCategory)
admin.site.register(MealCategory)

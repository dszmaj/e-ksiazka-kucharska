from django.contrib import admin
from products.models import ProductCategory
from recipes.models import MealCategory


admin.site.register(ProductCategory)
admin.site.register(MealCategory)

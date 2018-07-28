from django.contrib import admin
from meals.models import Meal, MealCategory, MealComment

admin.site.register(Meal)
admin.site.register(MealCategory)
admin.site.register(MealComment)
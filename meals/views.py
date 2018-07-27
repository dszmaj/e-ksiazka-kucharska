from django.shortcuts import render, get_object_or_404
from meals.models import Meal


def meal_add():
    pass


def meal_delete():
    pass


def meal_edit():
    pass


def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    return render(request, 'meals/meal_detail.html', {'meal': meal})


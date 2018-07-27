from django.shortcuts import render, get_object_or_404
from meals.models import Meal, MealComment
from meals.forms import MealCommentForm


def meal_add():
    pass


def meal_delete():
    pass


def meal_edit():
    pass


def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    meal_comments = meal.comments.all()
    if request.method == 'POST':
        meal_comment_form = MealCommentForm(request.POST)
        if meal_comment_form.is_valid():
            new_comment = meal_comment_form.save(commit=False)
            new_comment.meal = meal
            new_comment.user = request.user
            new_comment.save()
    else:
        meal_comment_form = MealCommentForm()
    return render(request, 'meals/meal_detail.html',
                  {'meal': meal, 'meal_comments': meal_comments, 'meal_comment_form': meal_comment_form})


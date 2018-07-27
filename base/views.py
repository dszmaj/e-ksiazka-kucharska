from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from meals.models import Meal


@login_required
def dashboard(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'meals': meals})


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard/')
    else:
        return render(request, 'index.html', {'index': index})


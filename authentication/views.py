from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from authentication.forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': dashboard})

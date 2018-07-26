from django.urls import path
from base.views import dashboard

app_name = 'base'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]

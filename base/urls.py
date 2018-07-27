from django.urls import path
from base.views import index, dashboard

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]

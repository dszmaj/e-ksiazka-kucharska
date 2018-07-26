from django.urls import path
from base.views import root, dashboard

app_name = 'base'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('', root, name='root_view'),
]

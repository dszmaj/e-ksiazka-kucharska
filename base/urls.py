from django.urls import path
from base.views import root

app_name = 'base'

urlpatterns = [
    path('', root, name='root_view'),
]

from django.urls import path
from meals.views import meal_add, meal_delete, meal_detail, meal_edit

app_name = 'meals'

urlpatterns = [
    path('add/', meal_add, name='meal_add'),
    path('<int:pk>/', meal_detail, name='meal_detail'),
    path('<int:pk>/delete/', meal_delete, name='meal_delete'),
    path('<int:pk>/edit/', meal_edit, name='meal_edit'),

]

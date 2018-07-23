from django.urls import path
from categories.views import category_add, category_delete, category_detail, category_edit, category_list

app_name = 'categories'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('add/', category_add, name='category_add'),
    path('<int:pk>/', category_detail, name='category_detail'),
    path('<int:pk>/delete/', category_delete, name='category_delete'),
    path('<int:pk>/edit/', category_edit, name='category_edit'),

]

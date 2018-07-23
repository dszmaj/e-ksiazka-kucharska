from django.urls import path
from products.views import product_add, product_delete, product_detail, product_edit, product_list

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', product_add, name='product_add'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/delete/', product_delete, name='product_delete'),
    path('<int:pk>/edit/', product_edit, name='product_edit'),

]
from django.urls import path
from users.views import dashboard, user_detail, profile_edit

app_name = ''

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('users/<username>/', user_detail, name='user_detail'),
    path('users/<username>/edit/', profile_edit, name='profile_edit'),
]
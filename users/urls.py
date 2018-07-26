from django.urls import path
from users.views import user_detail, profile_edit

app_name = 'users'

urlpatterns = [

    path('<username>/', user_detail, name='user_detail'),
    path('<username>/edit/', profile_edit, name='profile_edit'),
]

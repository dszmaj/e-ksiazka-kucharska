from django.urls import path
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done,\
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from authentication.views import register

app_name = ''

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('password-change/', password_change, {'post_change_redirect': 'password_change_done'}, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),
    path('password-reset/', password_reset, {'post_reset_redirect': 'password_reset_done'}, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),

]

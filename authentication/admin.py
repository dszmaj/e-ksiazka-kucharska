from django.contrib import admin
from authentication.models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'photo']


admin.site.register(UserProfile, ProfileAdmin)

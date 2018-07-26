from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    SEX_CHOICES = (
        ('female', _('Female')),
        ('male', _('Male')),
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User profile{}'.format(self.user)

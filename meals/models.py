from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class MealCategory(models.Model):  # adding only from admin panel
    # meals from Meal model
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MealComment(models.Model):
    body = models.TextField(_('Content'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Meal(models.Model):
    # products from Product model
    recipe = models.TextField(_('Directions'), null=True)
    categories = models.ManyToManyField(MealCategory, related_name='meals')
    comments = models.ManyToManyField(MealComment, related_name='meals')
    photo = models.ImageField(_('Photo'), upload_to='images/%Y/%m/%d/', blank=True, null=True)
    PREPARATION_TIME_CHOICES = (
        ('very_fast', _('under 15 minutes')),
        ('fast', _('15 - 30 minutes')),
        ('medium', _('30 - 60 minutes')),
        ('long', _('more then 60 minutes')),
    )
    preparation_time = models.CharField(
        _('preparation time'), max_length=50, choices=PREPARATION_TIME_CHOICES, default='fast')

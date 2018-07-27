from django.forms import ModelForm

from meals.models import MealComment


class MealCommentForm(ModelForm):
    class Meta:
        model = MealComment
        fields = ['body']

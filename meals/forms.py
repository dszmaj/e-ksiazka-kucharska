from django.forms import ModelForm, Textarea
from meals.models import MealComment


class MealCommentForm(ModelForm):
    class Meta:
        model = MealComment
        fields = ['body']
        widgets = {'body': Textarea()}

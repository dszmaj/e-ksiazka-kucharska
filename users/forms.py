from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
from users.models import UserProfile


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'photo', 'sex')
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from users.forms import UserEditForm, UserProfileEditForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


@login_required
def profile_edit(request, username):
    userprofile = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('The update of the profile was successful'))
        else:
            messages.error(request, _('An error occurred while updating the profile'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
    return render(request, 'user_account/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form,
                                                              'userprofile': userprofile})


@login_required
def user_detail(request, username):
    userprofile = get_object_or_404(User, username=username)
    return render(request, 'user_account/profile.html', {'userprofile': userprofile})

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class EditPerfilForm(UserChangeForm):

    class meta:
        model = User
        fields = ('username',
            'email',
            'first_name',
            'last_name',
            'password',
         )
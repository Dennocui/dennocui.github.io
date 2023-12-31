from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Club, ClubAdmin, HighSchool, Position
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, DateInput


class ClubForm(BSModalForm):
    class Meta:
        model = Club
        fields = '__all__'


class ClubAdminForm(BSModalForm):
    class Meta:
        model = ClubAdmin
        fields = '__all__'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pages.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'description', 'website', 'places_visited']



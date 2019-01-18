from django import forms
from django.contrib.auth.models import User
from chatterApp.models import ChatterUser

class ChatterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username", "email", "password")



class ChatterUserProfileForm(forms.ModelForm):
    class Meta():
        model = ChatterUser
        fields = ("profile_pic",)

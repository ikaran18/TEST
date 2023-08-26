from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=25)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')
        
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=25)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')
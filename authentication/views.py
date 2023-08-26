from django.views import generic
from django.contrib.auth.forms import UserChangeForm 
from .forms import SignUpForm,EditProfileForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterForm(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/user_signup.html"
    success_url = reverse_lazy('login')


class UserEditProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/editprofile.html"
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
    


from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserUpdateForm, PasswordUpdateForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

#update user data
class UpdateUserView(generic.UpdateView):
    form_class = UserUpdateForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
     return self.request.user


#password change view
class UserPasswordChangeView(PasswordChangeView):
   form_class = PasswordUpdateForm
   success_url = reverse_lazy('home')



   
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm, EditProfileForm, PasswordChangeingForm,ProfilePageForm,EditProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from sukeachin.models import profile


class UserRegistration(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserProfileEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeingForm
    success_url = reverse_lazy('home')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ShowProfilePage(generic.DetailView):
    model = profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):

        page_user = get_object_or_404(profile, id=self.kwargs['pk'])
        context = super(ShowProfilePage, self).get_context_data(
            *args, **kwargs)
        context['page_user'] = page_user
        return context

class  EditProfilePageView(generic.UpdateView):
    model = profile
    template_name = 'registration/edit_profile_page.html'
    form_class = EditProfilePageForm
    success_url = reverse_lazy('home')

class createProfile(generic.CreateView):
    model = profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
   

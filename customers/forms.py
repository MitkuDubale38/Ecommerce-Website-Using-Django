from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from sukeachin.models import profile

class ProfilePageForm(forms.ModelForm):
  class Meta:
        model = profile
        fields = ('bio','profile_pic')

        widgets = {

            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profile_pic': forms.FileField(),
            

    }

class EditProfilePageForm(forms.ModelForm):
  class Meta:
        model = profile
        fields = ('bio','profile_pic')

        widgets = {

            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profile_pic': forms.FileField(),
            

    }

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__ (self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password','date_joined' )

class PasswordChangeingForm(PasswordChangeForm):


    old_password = forms.CharField(max_length=100,widget = forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100,widget = forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2= forms.CharField(max_length=100,widget = forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    
    class Meta:
        model = User
        fields = (' old_password', 'new_password1', 'new_password2')
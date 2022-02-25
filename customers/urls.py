from django.urls import path
from .views import UserRegistration, UserProfileEdit, PasswordsChangeView, ShowProfilePage, EditProfilePageView,createProfile
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   

    path('register/', UserRegistration.as_view(), name="register"),
    path('edit_profile/', UserProfileEdit.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(
        template_name="registration/change_password.html")),
    path('password_success/',views.password_success, name="password_success" ),
    path('<int:pk>/profile', ShowProfilePage.as_view(), name="show_profile_page" ),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name="edit_profile_page" ),
    path('create_profile_page/', createProfile.as_view(), name="create_profile_page" ),
   
    #password reset view
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),      
    

]

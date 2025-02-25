from django.urls import path
from . import views
from allauth.account.views import (
    LoginView, 
    SignupView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetFromKeyView,
)
from django.contrib.auth import logout

urlpatterns = [
    path('', views.home_view, name='home'),             # Public home page
    path("login/", LoginView.as_view(template_name="login.html"), name="account_login"),
    path("register/", SignupView.as_view(template_name="register.html"), name="account_signup"),
    path('logout/', views.logout_view, name='logout'),  # Logout
    
    # Password reset
    path("password-reset/", PasswordResetView.as_view(template_name="password_reset.html"), name="account_reset_password"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="account_reset_password_done"),
    path("password-reset-confirm/<uidb36>/<token>/", PasswordResetFromKeyView.as_view(template_name="password_reset_confirm.html"), name="account_reset_password_confirm"),
    
]
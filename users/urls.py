from django.urls import path
from . import views
from allauth.account.views import (
    LoginView, 
    SignupView,
    PasswordResetView,
    PasswordResetDoneView,
    EmailVerificationSentView,
)

urlpatterns = [
    path('', views.home_view, name='home'),
    path("login/", LoginView.as_view(template_name="login.html"), name="account_login"),
    path("register/", SignupView.as_view(template_name="register.html"), name="account_signup"),
    path('logout/', views.logout_view, name='logout'),  
    
    path("password-reset/", PasswordResetView.as_view(template_name="password_reset.html"), name="account_reset_password"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="account_reset_password_done"),
    path("email-verification/", EmailVerificationSentView.as_view(template_name="email_verification_sent.html"), name="account_email_verification_sent"),
    path("resend-verification/", views.resend_verification_email, name="account_resend_verification"),
    
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-a-resume/', views.create_a_resume_view, name='create_a_resume'),
]

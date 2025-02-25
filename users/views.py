from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from allauth.account.views import LoginView, SignupView, LogoutView


def home_view(request):
    """
    Public home page view.
    """
    return render(request, 'home.html')


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('home')



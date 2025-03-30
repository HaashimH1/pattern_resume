from django.urls import path, include
from allauth.socialaccount.providers.google.views import oauth2_login, oauth2_callback
from allauth.account.views import LoginView

urlpatterns = [
    # Google OAuth2 login and callback URLs
    path('social/google/login/', oauth2_login, name='google_login'),
    path('social/google/callback/', oauth2_callback, name='google_callback'),
    path('login/', LoginView.as_view(template_name="login.html"), name="socialaccount_login_cancelled"),

    # Include all relevant password reset URLs from allauth
    path('password/reset/key/', include('allauth.account.urls')),
]
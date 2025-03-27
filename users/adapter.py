from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # If user is already logged in, do nothing.
        if request.user.is_authenticated:
            return

        # Try to find an existing user with the same email address.
        email_address = sociallogin.account.extra_data.get('email')
        if not email_address:
            return

        # Search for a user with this email address.
        try:
            user = self.get_user(email_address)
        except Exception:
            user = None

        if user:
            # Connect the social account to the existing user.
            sociallogin.connect(request, user)

    def get_user(self, email):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            return User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return None

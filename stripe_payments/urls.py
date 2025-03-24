from django.urls import path
from .views import buy_template, stripe_webhook, checkout_success, checkout_cancel

urlpatterns = [
    path('buy_template/<int:template_id>/', buy_template, name='buy_template'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('checkout_success/', checkout_success, name='checkout_success'),
    path('checkout_cancel/', checkout_cancel, name='checkout_cancel'),
]
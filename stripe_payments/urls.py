from django.urls import path
from .views import buy_template, stripe_webhook, checkout_success, checkout_cancel
from . import views

urlpatterns = [
    path('buy_template/<int:template_id>/', buy_template, name='buy_template'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('checkout_success/<int:template_id>/', views.checkout_success, name='checkout_success'),
    path('checkout_cancel/<int:template_id>/', views.checkout_cancel, name='checkout_cancel'),
]
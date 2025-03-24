import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# utils
from users.utils import does_user_own_template
from .utils import create_checkout_session, update_user_status, record_order

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def buy_template(request, template_id):
    """
    If the user already owns the template, redirect to home.
    Otherwise, create a Stripe Checkout session and redirect the user to it.
    """
    if does_user_own_template(request.user, template_id):
        # will redirect to a more suitable URL later in production
        return redirect('home')
    
    session = create_checkout_session(request.user, template_id, request)
    return redirect(session.url)

@csrf_exempt
def stripe_webhook(request):
    """
    Stripe webhook endpoint.
    On checkout.session.completed, updates the user's status and creates an Order record.
    """
    print("Webhook received")
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    secret = settings.STRIPE_WEBHOOK_SECRET
    if secret is None:
        print("STRIPE_WEBHOOK_SECRET is not set!")
        return HttpResponse(status=400)
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, secret
        )
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        print("Webhook signature verification failed:", e)
        return HttpResponse(status=400)
    
    if event.get('type') == 'checkout.session.completed':
        session = event['data']['object']
        metadata = session.get('metadata', {})
        user_id = metadata.get('user_id')
        template_id = metadata.get('template_id')
        stripe_charge_id = session.get('payment_intent')  # PaymentIntent ID
        amount_total = session.get('amount_total', 0) / 100.0  # convert pence to pounds
        
        print("1")
        
        if user_id and template_id:
            print("2")
            User = get_user_model()
            user = get_object_or_404(User, id=user_id)
            print("3")
            update_user_status(user, template_id)
            record_order(user, template_id, stripe_charge_id, amount_total)
    
    print("Webhook processed successfully")
    return HttpResponse(status=200)

def checkout_success(request):
    """
    A simple success view for a successful checkout.
    """
    return HttpResponse("Payment succeeded. Your template has been purchased.")

def checkout_cancel(request):
    """
    A simple view for a canceled checkout session.
    """
    return HttpResponse("Payment canceled. Please try again.")

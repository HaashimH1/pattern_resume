from django.shortcuts import get_object_or_404
from users.models import Template, UserStatus, Order
from django.conf import settings

def create_checkout_session(user, template_id, request):
    """
    Creates a Stripe Checkout session for the given template purchase.
    """
    template_obj = get_object_or_404(Template, id=template_id)
    # Convert price to pence
    price_in_pence = int(template_obj.price * 100)
    
    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'unit_amount': price_in_pence,
                'product_data': {
                    'name': template_obj.name,
                    'description': template_obj.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            f"/stripe/checkout_success/{template_id}/?session_id={{CHECKOUT_SESSION_ID}}"
        ),
        cancel_url=request.build_absolute_uri(
            f"/stripe/checkout_cancel/{template_id}/?session_id={{CHECKOUT_SESSION_ID}}"
        ),
        metadata={
            'user_id': user.id,
            'template_id': template_obj.id,
        }
    )
    return session

def update_user_status(user, template_id):
    """
    Updates the user's status by adding the purchased template.
    If the user hasn't purchased before (has_purchased is False), updates it to True.
    """
    print("Updating user status")
    user_status, created = UserStatus.objects.get_or_create(
        user=user,
        defaults={'has_purchased': False}
    )
    if not user_status.has_purchased:
        user_status.has_purchased = True
    if not user_status.templates.filter(id=template_id).exists():
        template_obj = get_object_or_404(Template, id=template_id)
        user_status.templates.add(template_obj)
    user_status.save()
    return user_status

def record_order(user, template_id, stripe_charge_id, amount):
    """
    Creates an Order record for a completed purchase.
    """
    print("Recording order")
    template_obj = get_object_or_404(Template, id=template_id)
    order = Order.objects.create(
        user=user,
        template=template_obj,
        stripe_charge_id=stripe_charge_id,
        amount=amount
    )
    return order

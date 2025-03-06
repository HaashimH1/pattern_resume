from .models import UserStatus, Template, Order, Resume
from django.core.exceptions import ObjectDoesNotExist

def get_user_status(user):
    """
    Retrieves the UserStatus for the given user. If it doesn't exist, creates one.
    Returns a dictionary with user status information.
    """
    user_status, created = UserStatus.objects.get_or_create(
        user=user,
        defaults={'has_purchased': False}
    )
    
    status_data = {
        'has_purchased': user_status.has_purchased,
        'templates': list(user_status.templates.all().values())  # Returns list of dictionaries for templates
    }
    
    return status_data

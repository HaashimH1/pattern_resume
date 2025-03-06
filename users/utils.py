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


def is_resume_created(user):
    return Resume.objects.filter(user=user).exists()

def does_user_own_template(user, template_id):
    try:
        user_status = UserStatus.objects.get(user=user)
        return user_status.templates.filter(id=template_id).exists()
    except ObjectDoesNotExist:
        return False

def create_resume(user, template_id):

    template_id = int(template_id)
    if not does_user_own_template(user, template_id):
        return None  # User does not own the chosen template
    else:
        template_instance = Template.objects.get(id=template_id)
        resume = Resume.objects.create(
            user=user,
            template=template_instance,
            job_title="Job Title",
            summary="Your Summary Here"
        )
    
    return resume
from .models import UserStatus, Template, Order, Resume, ResumeSection, ResumeSubSection
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
        )
    
    return resume


def get_resume_data(user):
    try:
        resume_data = Resume.objects.get(user=user)
        return resume_data
    except ObjectDoesNotExist:
        return None
    
def create_section(resume, section_name):
    section = ResumeSection.objects.create(
        resume=resume,
        name=section_name,
        order=get_section_count(resume.user) + 1
    )
    return section
    
def get_sections(user):
    return ResumeSection.objects.filter(resume__user=user).order_by('order')
    
def get_section_count(user):
    return ResumeSection.objects.filter(resume__user=user).count()

def get_subsection_count(user, section_id):
    return ResumeSubSection.objects.filter(section__resume__user=user, section__id=section_id).count()
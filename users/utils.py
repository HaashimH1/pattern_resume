from .models import UserStatus, Template, Resume, ResumeSection, ResumeSubSection
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
    
def get_sections(user):
    return ResumeSection.objects.filter(resume__user=user).order_by('order')
    
def get_section_count(user):
    return ResumeSection.objects.filter(resume__user=user).count()

def get_subsection_count(user, section_id):
    return ResumeSubSection.objects.filter(section__resume__user=user, section__id=section_id).count()


def save_resume(user, data):
    try:
        resume = Resume.objects.get(id=data.get("resume_id"), user=user)
    except Resume.DoesNotExist:
        print("Resume does not exist")
        return

    # Validate and update fields
    if validate_field_length(data.get("job_title"), Resume._meta.get_field("job_title").max_length):
        resume.job_title = data.get("job_title")
    else:
        print("Job title exceeds maximum length and was not updated.")

    if validate_field_length(data.get("fname"), Resume._meta.get_field("first_name").max_length):
        resume.first_name = data.get("fname")
    else:
        print("First name exceeds maximum length and was not updated.")

    if validate_field_length(data.get("lname"), Resume._meta.get_field("last_name").max_length):
        resume.last_name = data.get("lname")
    else:
        print("Last name exceeds maximum length and was not updated.")

  
    


    if validate_field_length(data.get("phone"), Resume._meta.get_field("phone_number").max_length):
        resume.phone_number = data.get("phone")
    else:
        print("Phone number exceeds maximum length and was not updated.")

    if validate_field_length(data.get("city"), Resume._meta.get_field("city").max_length):
        resume.city = data.get("city")
    else:
        print("City exceeds maximum length and was not updated.")

    resume.email = data.get("email")
    resume.summary = data.get("summary")

    resume.save()


def save_subsection(user, data):
    try:
        sub = ResumeSubSection.objects.get(
            id=data.get("sub_id"),
            section__resume__user=user
        )
    except ResumeSubSection.DoesNotExist:
        print("Subsection does not exist or does not belong to the user")
        return

    # Validate and update the title field
    if validate_field_length(data.get("sub_title"), ResumeSubSection._meta.get_field("title").max_length):
        sub.title = data.get("sub_title")
    else:
        print("Subsection title exceeds maximum length and was not updated.")

    sub.description = data.get("sub_desc")

    sub.save()


def save_section_name(user, data):
    try:
        section = ResumeSection.objects.get(
            id=data.get("section_id"),
            resume__user=user
        )
    except ResumeSection.DoesNotExist:
        print("Section does not exist or does not belong to the user")
        return

    # Validate and update the section name
    if validate_field_length(data.get("section_name"), ResumeSection._meta.get_field("name").max_length):
        section.name = data.get("section_name")
        section.save()
    else:
        print("Section name exceeds maximum length and was not updated.")


def add_subsection(user, section_id):
    try:
        section = ResumeSection.objects.get(id=section_id, resume__user=user)
    except ResumeSection.DoesNotExist:
        print("Section does not exist or does not belong to the user")
        return None

    order = get_subsection_count(user, section_id) + 1

    subsection = ResumeSubSection.objects.create(
        section=section,
        title= f"Subsection {order}",
        description= f"Description for this sub",
        order=order
    )

    return subsection


def add_section(user, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id, user=user)
    except Resume.DoesNotExist:
        print("Resume does not exist or does not belong to the user")
        return None

    order = get_section_count(user) + 1

    section = ResumeSection.objects.create(
        resume=resume,
        name=f"Section {order}",
        order=order
    )

    return section

def delete_subsection(user, sub_id):
    try:
        sub = ResumeSubSection.objects.get(id=sub_id, section__resume__user=user)
        section_id = sub.section.id
        sub.delete()
        rearrange_subsection_orders(user, section_id)
    except ResumeSubSection.DoesNotExist:
        print("Subsection does not exist or does not belong to the user")

def rearrange_subsection_orders(user, section_id):
    subsections = ResumeSubSection.objects.filter(section__id=section_id, section__resume__user=user).order_by('order')
    for i, sub in enumerate(subsections):
        sub.order = i + 1
        sub.save()
        
def delete_section(user, section_id):
    try:
        section = ResumeSection.objects.get(id=section_id, resume__user=user)
        resume_id = section.resume.id
        section.delete()
        rearrange_section_orders(user, resume_id)
    except ResumeSection.DoesNotExist:
        print("Section does not exist or does not belong to the user")

def rearrange_section_orders(user, resume_id):
    sections = ResumeSection.objects.filter(resume__id=resume_id, resume__user=user).order_by('order')
    for i, section in enumerate(sections):
        section.order = i + 1
        section.save()
        
def change_template(user, template_id):
    try:
        resume = Resume.objects.get(user=user)
    except Resume.DoesNotExist:
        print("Resume does not exist")
        return
    
    if not does_user_own_template(user, template_id):
        print("User does not own the chosen template")
        return None  # User does not own the chosen template
    else:
        resume.template = Template.objects.get(id=template_id)
        resume.save()
        
    return resume


def get_template_content(user):
    """
    Returns a dictionary containing the HTML and CSS content from the template 
    associated with the user's resume.
    """
    try:
        resume = Resume.objects.get(user=user)
        template_instance = resume.template
        return {
            "html": template_instance.html_content,
            "css": template_instance.css_content,
        }
    except Resume.DoesNotExist:
        return {"html": "", "css": ""}  # No resume exists for this user
    
    
def swap_sub(user, sub_a_id, sub_b_id):
    try:
        sub_a = ResumeSubSection.objects.get(id=sub_a_id, section__resume__user=user)
        sub_b = ResumeSubSection.objects.get(id=sub_b_id, section__resume__user=user)
        
        # Swap the order values
        sub_a.order, sub_b.order = sub_b.order, sub_a.order
        
        # Save the changes
        sub_a.save()
        sub_b.save()
        
    except ResumeSubSection.DoesNotExist:
        print("One or both subsections do not exist or do not belong to the user")
        
        
def swap_section(user, section_a_id, section_b_id):
    try:
        section_a = ResumeSection.objects.get(id=section_a_id, resume__user=user)
        section_b = ResumeSection.objects.get(id=section_b_id, resume__user=user)
        
        # Swap the order values
        section_a.order, section_b.order = section_b.order, section_a.order
        
        # Save the changes
        section_a.save()
        section_b.save()
        
    except ResumeSection.DoesNotExist:
        print("One or both sections do not exist or do not belong to the user")
        
        
        
def get_all_templates():
    return Template.objects.all().order_by('id').values()   # Returns list of dictionaries for templates
        
        
def validate_field_length(value, max_length):
    """
    Validates that the given value does not exceed the specified max_length.
    Returns True if valid, False otherwise.
    """
    return len(value) <= max_length if value else True
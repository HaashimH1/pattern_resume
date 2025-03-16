from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from allauth.account.models import EmailAddress 
from users.utils import (
    get_user_status,
    is_resume_created,
    create_resume,
    get_resume_data,
    get_sections,
    save_resume,
    save_subsection,
    save_section_name,
    add_subsection,
    )


def home_view(request):
    """
    Public home page view.
    """
    if request.user.is_authenticated:
        user_status_data = get_user_status(request.user)
        return render(request, 'home.html', {"db_access": user_status_data['has_purchased']})
    else:
        return render(request, 'home.html')


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('home')


def resend_verification_email(request):
    if request.user.is_authenticated:
        email_address = EmailAddress.objects.filter(user=request.user, verified=False).first()
        if email_address:
            email_address.send_confirmation(request)
            messages.success(request, "A new verification email has been sent to your inbox.")
        else:
            messages.info(request, "Your email is already verified.")

    return redirect("account_email_verification_sent")

def create_a_resume_view(request):
    
    if not request.user.is_authenticated:
        return redirect('account_login')
    else: 
        user_status_data = get_user_status(request.user)
        if not user_status_data['has_purchased']:
            return redirect('home')
        elif is_resume_created(request.user):
            return redirect('dashboard')
        else:
            if request.method == 'POST' and "create_resume" in request.POST:
                handle_creating_resume(request)
                return redirect('dashboard')
            
            return render(request, 'create_a_resume.html', {
            'templates': user_status_data['templates']
        })


def dashboard_view(request):
    """
    Dashboard view for authenticated users.
    """
    if not request.user.is_authenticated:
        return redirect('account_login')
    else:
        user_status_data = get_user_status(request.user)
        if user_status_data['has_purchased']:
            does_resume_exist = is_resume_created(request.user)
            if not does_resume_exist:
                return redirect('create_a_resume') 
            
            # Dashboard access from here 
            resume_data = get_resume_data(request.user)
            sections_data = get_sections(request.user)
            
            if request.method == "POST":
                if "save_resume" in request.POST:
                    handle_saving_resume(request)
                elif "save_subsection" in request.POST:
                    handle_saving_subsection(request)
                elif "save_section_name" in request.POST:
                    handle_saving_section_name(request)
                elif "add_sub" in request.POST:
                    handle_adding_sub(request)
                    
                return redirect('dashboard') # Make sure to redirect
            
            
            return render(request, 'dashboard.html', {
                'resume_data': resume_data,
                "sections_data": sections_data,
                
                })
        else:
            return redirect('home')   
        
        
        
def handle_creating_resume(request):

    template_id = request.POST.get('template_id')
    try:
        create_resume(request.user, template_id)
        print("Resume created successfully")
    except Exception as e:
        print(f"Error creating resume: {e}")
        
        
    
    
def handle_saving_resume(request):

    data = {
        'resume_id': request.POST.get('resume_id'),
        'job_title': request.POST.get('job_title'),
        'fname': request.POST.get('fname'),
        'lname': request.POST.get('lname'),
        'email': request.POST.get('email'),
        'phone': request.POST.get('phone'),
        'city': request.POST.get('city'),
        'summary': request.POST.get('summary'),
    }
            
        
     
    save_resume(request.user, data)
    
    
    
def handle_saving_subsection(request):
    
    save_subsection(request.user, {
        "sub_id": request.POST.get('sub_id'),
        "sub_title": request.POST.get('sub_title'),
        "sub_desc": request.POST.get('sub_desc')
    })
    
    
def handle_saving_section_name(request):
    
    save_section_name(request.user,{
        "section_id": request.POST.get('section_id'),
        "section_name": request.POST.get('section_name'),
    })
    
    
def handle_adding_sub(request):
    
    add_subsection(request.user, request.POST.get('section_id'))
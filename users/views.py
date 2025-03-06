from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from allauth.account.models import EmailAddress 
from users.utils import (
    get_user_status,
    is_resume_created,
    create_resume,
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
            return render(request, 'dashboard.html')
        else:
            return redirect('home')
        
        
        
def handle_creating_resume(request):

    template_id = request.POST.get('template_id')
    try:
        create_resume(request.user, template_id)
        print("Resume created successfully")
    except Exception as e:
        print(f"Error creating resume: {e}")
        
        
    
    
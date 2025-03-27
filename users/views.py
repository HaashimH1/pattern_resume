import io
from django.http import HttpResponse
from django.template import Template, Context
from xhtml2pdf import pisa
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
    add_section,
    delete_subsection,
    delete_section,
    change_template,
    get_template_content,
    swap_sub,
    swap_section,
    get_all_templates,
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


def view_templates(request):
    return render(request, 'view_templates.html',{
        "templates": get_all_templates()
    })
    
def orders_view(request):
    
    if not request.user.is_authenticated:
        return redirect('account_login')

    return render(request, 'orders.html', {
        "templates": request.user.userstatus.templates.all,
    })

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
            template_data = get_template_content(request.user)
            
            # Create the context for rendering the stored template
            render_context = {
                'resume_data': resume_data,
                'sections_data': sections_data,
            }
            # Compile and render the stored HTML template with the context
            rendered_resume = Template(template_data['html']).render(Context(render_context))
                
            if request.method == "POST":
                print(request.POST)
                if "save_resume" in request.POST:
                    handle_saving_resume(request)
                elif "save_subsection" in request.POST:
                    handle_saving_subsection(request)
                elif "save_section_name" in request.POST:
                    handle_saving_section_name(request)
                elif "add_sub" in request.POST:
                    handle_adding_sub(request)
                elif "add_section" in request.POST:
                    handle_adding_section(request)
                elif "delete_sub" in request.POST:
                    handle_deleting_sub(request)
                elif "delete_section" in request.POST:
                    handle_deleting_section(request)
                elif "change_template" in request.POST:
                    handle_change_template(request)
                elif "swap_sub" in request.POST:
                    handle_swap_sub(request)
                elif "swap_section" in request.POST:
                    handle_swap_section(request)
                
                    
                    
                    
                return redirect('dashboard') # Make sure to redirect
            
            
            return render(request, 'dashboard.html', {
                'resume_data': resume_data,
                'sections_data': sections_data,
                'rendered_resume': rendered_resume,
                'template_css': template_data['css'],
                'user_status_data': user_status_data,
                
                })
        else:
            return redirect('home')   
          
          
def download_resume_pdf(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    # Ensure user has a resume created
    if not is_resume_created(request.user):
        return redirect('create_a_resume')
    
    # Get resume data and sections
    resume_data = get_resume_data(request.user)
    sections_data = get_sections(request.user)
    
    template_data = get_template_content(request.user)
    
    # Create the context to be used in the template
    render_context = {
        'resume_data': resume_data,
        'sections_data': sections_data,
    }
    
    # Render the stored HTML template (which is a string) with the context
    rendered_html = Template(template_data['html']).render(Context(render_context))
    
    # Build a complete HTML document by injecting the CSS into a <style> tag
    html_string = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>{resume_data.first_name} {resume_data.last_name} - Resume</title>
      <style>
        {template_data['css']}
      </style>
    </head>
    <body>
      {rendered_html}
    </body>
    </html>
    """
    
    # Generate PDF using xhtml2pdf
    result = io.BytesIO()
    pdf = pisa.CreatePDF(io.StringIO(html_string), dest=result)
    
    if not pdf.err:
        # Return PDF as an inline response (opens in a new tab)
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        return response
    else:
        return HttpResponse("Error generating PDF", status=400)
        

        
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
    add_subsection(request.user, request.POST.get("section_id"))
    
    
def handle_adding_section(request):
    add_section(request.user, request.POST.get("resume_id"))
    
    
def handle_deleting_sub(request):
    delete_subsection(request.user, request.POST.get("sub_id"))
    
def handle_deleting_section(request):
    delete_section(request.user, request.POST.get("section_id"))
    
def handle_change_template(request):
    change_template(request.user, request.POST.get("template_id"))
    
    
def handle_swap_sub(request):
   swap_sub(request.user, request.POST.get("sub_a_id"), request.POST.get("sub_b_id"))
   
   
def handle_swap_section(request):
    swap_section(request.user, request.POST.get("section_a_id"), request.POST.get("section_b_id"))
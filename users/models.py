from django.conf import settings
from django.db import models

class UserStatus(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_purchased = models.BooleanField(default=False)
    templates = models.ManyToManyField('Template', blank=True)
    
    def __str__(self):
        # This will display as "username's status" in the admin panel
        return f"{self.user.username}'s status"

class Template(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    html_content = models.TextField()
    css_content = models.TextField()
    img_url = models.TextField()
    
    def __str__(self):
        return self.name  # This will show the template's title in the admin panel

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}" # This will show the order's title in the admin panel

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    first_name = models.CharField(max_length=30, default="First name")
    last_name = models.CharField(max_length=30, default="Last name")
    job_title = models.CharField(max_length=30, default="Job title")
    email = models.TextField(default="Email Address")
    phone_number = models.CharField(max_length=20, default="Phone number")
    city = models.CharField(max_length=30, default="City")
    last_saved = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Resume"


class ResumeSection(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=30)
    order = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.resume.user.username} - {self.name}: Resume Section"


class ResumeSubSection(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, related_name='sub')
    title = models.CharField(max_length=60)
    description = models.TextField()
    order = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.section.resume.user.username} - {self.section.name} > {self.title}: Resume SubSection"


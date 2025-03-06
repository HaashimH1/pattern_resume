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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    job_title = models.CharField(max_length=255)
    summary = models.TextField()
    last_saved = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Resume"  # This will show the resume's title in the admin panel


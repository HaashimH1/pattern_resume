from django.contrib import admin
from .models import UserStatus, Template, Order, Resume

admin.site.register(UserStatus)
admin.site.register(Template)
admin.site.register(Order)
admin.site.register(Resume)

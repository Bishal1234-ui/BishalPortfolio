from django.contrib import admin
from .models import project, skill, certificate

# Register your models here.

admin.site.register(project)
admin.site.register(skill)
admin.site.register(certificate)

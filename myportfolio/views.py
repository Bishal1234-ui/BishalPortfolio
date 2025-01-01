from django.shortcuts import render
from .models import skill, project, certificate
import json

# Create your views here.



def home(request):
    skill_list = skill.objects.all()
    project_list = project.objects.all()
    certificate_list = certificate.objects.all()
    
    context = {
        "skill_list" : skill_list,
        "project_list" : project_list,
        "certificate_list" : certificate_list
    }
    return render(request, "myportfolio/home.html", context)

def projects(request):
    project_list = project.objects.all()
    # for proj in project_list:
    #     proj.techstack = json.loads(proj.techstack)
    context = {
        "project_list" : project_list,
    }
    return render(request, "myportfolio/projects.html", context)
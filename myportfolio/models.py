from django.db import models

# Create your models here.


# For my portfolio I need a project Object for adding projects in the project page
class project(models.Model):
    title = models.CharField(max_length=200)
    techstack = models.JSONField()
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    image = models.URLField(max_length=200, default="www.google.com")

    def __str__(self):
        return self.title


# skills and proficiency  ( here programming )   
class skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# certification
class certificate(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()


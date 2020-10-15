from django.db import models

# Create your models here.

class department_hods(models.Model):
    full_name = models.CharField(max_length=50)
    cnic = models.DecimalField(max_digits=15)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class exams(models.Model):
    pass

    
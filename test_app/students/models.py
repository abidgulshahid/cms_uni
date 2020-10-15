from django.db import models

# Create your models here.

class registration(models.Model):
    full_name = models.CharField(max_length=50,help_text="Enter Your Full Name")
    cnic = models.CharField(max_length=15,help_text="Enter Your Correct CNIC")
    email = models.CharField(max_length=20, help_text='Enter Your Email')
    password = models.CharField(max_length=100, help_text='Enter Your Password')
    
    def __str__(self):
        return self.full_name
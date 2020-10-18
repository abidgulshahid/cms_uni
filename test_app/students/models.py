from django.db import models

# Create your models here.

class registration(models.Model):
    full_name = models.CharField(max_length=50,help_text="Enter Your Full Name")
    semester = models.CharField(max_length=1)
    

class department(models.Model):
    dep = models.ForeignKey(registration, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


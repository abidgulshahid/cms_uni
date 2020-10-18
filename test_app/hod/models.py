from django.db import models

# Create your models here.

class department_hods(models.Model):
    full_name = models.CharField(max_length=50,help_text="Enter Your Full Name")
    cnic = models.CharField(max_length=15,help_text="Enter Your Correct CNIC")
    email = models.CharField(max_length=20, help_text='Enter Your Email')
    password = models.CharField(max_length=100, help_text='Enter Your Password')

    def __str__(self):
        return self.full_name


class departments(models.Model):
    dep_name = models.CharField(max_length=60, help_text="Enter Your Department Name: ")
    dep_hod = models.ForeignKey(department_hods, blank=True, null=True, on_delete=models.CASCADE)


class exams(models.Model):
    final_result_date = models.CharField(max_length=40)
    final_exam_date = models.CharField(max_length=40)
    mid_result_date = models.CharField(max_length=30)
    mid_final_date = models.CharField(max_length=40)
    dep_hods = models.ForeignKey(department_hods, blank=True, null=True, on_delete=models.CASCADE)



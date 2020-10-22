from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class signup(UserCreationForm):
# 	cnic = forms.CharField(label='Enter Your CNIC: ', max_length=14)
# 	email = forms.CharField(label='Enter Your Email: ',max_length=50)
# 	password = forms.CharField(label='Enter Your Password: ',max_length=50)
# 	class meta:
# 		model = User
# 		fields = ['username', 'email', 'password', 'password2'] 


class createuserform(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email']
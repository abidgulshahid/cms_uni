from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import createuserform

def index(request):
	return render(request,'index.html')



def register(request):
    form =  createuserform()
    if request.method == 'POST':
    	form = createuserform(request.POST)
    	if form.is_valid():
    		form.save()
    context = {'form':form}
    return render(request, 'register.html', context=context)






# def get_cred(request):
# 	if request.method == 'POST':
# 		form  = signup(request.POST)
# 		if form.is_valid():
# 			return render(request,'thanks.html',{'form':form})
# 	else:
# 		form = signup()
# 	return render(request, 'home.html', {'form':form})

#Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def index(request):
    return render(request, 'index.html')


def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'registration/register.html', context)


# class HomePageView(TemplateView):
#     template_name = 'index.html'


# class Register(TemplateView):
#     template_name = 'register.html'
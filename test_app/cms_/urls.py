from django.urls import path
#from .views import HomePageView
from . import views

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('',views.index,name='home'),
    path('account/signup/',views.signup,name='signup'),
]

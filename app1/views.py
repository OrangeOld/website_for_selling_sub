from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from app1.models import *
from django.views.generic import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.

class Customers(ListView):
    model=User
    template_name=r'main_page.html'
    context_object_name = 'clients'
    #paginate_by = 2

class Subs(ListView):
    model=Sub
    template_name=r'main_page.html'
    context_object_name = 'subs'

def handle_form(request):
    if request.method=='POST':
        form=BeachUser(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('succ')
    else:
        form=BeachUser()
    return render(request,r'test-form.html',{'form':form})

def Succesrent(request):
    '''
    ---------------ADD--------------------
    function that will send information about succesful rent
    to a seller (gmail, or telegram etc.)
    '''
    return render(request,r'Successful_rent.html')

def show_post(request,post_slug):
    'For posts'
    subobj=get_object_or_404(Sub,slug=post_slug)# seek an object using slug
    print(subobj.image)
    return render(request,r'sub_post.html',{'sub':subobj})

class RegisterUser(CreateView):
    form_class=UserCreationForm
    template_name = r'register.html'
    success_url = reverse_lazy('login')

    #Get dictionary
    '''def get_context_data(self, **kwargs):
        context=super().get_context_data(self,**kwargs)
        context.setdefault('',)
        return context
    '''

class LoginUser(LoginView):
    form_class=AuthenticationForm
    template_name = 'login.html'
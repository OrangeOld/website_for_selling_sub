from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from app1.models import *
from django.views.generic import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
import smtplib
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
        print(form.as_p())
        if form.is_valid():
            form.save()
            def send_notice():
                smtp_server = "smtp.gmail.com"
                port = 587
                username = ""
                password = ""
                sender_email = f"{form.cleaned_data.get('email')}"
                recipient_email = ""

                server = smtplib.SMTP(smtp_server, port)
                server.starttls()
                server.login(username, password)

                message = f"{form.cleaned_data.get('Name')} wants to rent a boat!!!"

                server.sendmail(sender_email, recipient_email, message)
                server.quit()
            #send_notice()
            return redirect('succ')
    else:
        form=BeachUser()
        #print(form.as_p())
        #print(form.cleaned_data.get(''))
    return render(request,r'test-form.html',{'form':form})

def Succesrent(request):
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
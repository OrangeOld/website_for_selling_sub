from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from . import models



class BeachUser(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['Name','Surname','Armchair_number','image','email']
        def __init__(self,*args,**kwargs):
            'redefine fields in form'
            super().__init__(*args,**kwargs)
            self.fields['Name'].widget.attrs.update({'class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp'})
            self.fields['email'].widget.attrs.update({'class':'form-control','id':'exampleInputEmail2','aria-describedby':'emailHelp'})
            self.fields['Surname'].widget.attrs.update({'class':'form-control','id':'exampleInputEmail3','aria-describedby':'emailHelp'})
            self.fields['Armchair_number'].widget.attrs.update({'class': 'form-control','aria-describedby': 'emailHelp'})
            self.fields['image'].widget.attrs.update({'class': 'form-control','aria-describedby': 'emailHelp'})
class RegisterUserForm(UserCreationForm):
    class Meta:
        model=models.User
        fields=('Name','Surname','email')
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-input'}),
            'Surname':forms.TextInput(attrs={'class':'form-input'}),
            'email':forms.TextInput(attrs={'class':'form-input'})
           # 'password_field':forms.PasswordInput(attrs={'':''})
        }

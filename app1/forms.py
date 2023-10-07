from django import forms
from django.utils import timezone
from . import models

class BeachUser(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['Name','Surname','Armchair_number','image','email']



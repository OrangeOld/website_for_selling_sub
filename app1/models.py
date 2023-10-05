from django.db import models
#from phonenumber_field.modelfields import *
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class User(models.Model):
    Name=models.TextField(max_length=15)
    Surname=models.TextField()
    Armchair_number=models.TextField()
   # phone_number=PhoneNumberField()
    Start_Date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.Name)
        super().save(*args,**kwargs)

class Sub(models.Model):
    Name = models.TextField(max_length=15)
    Number = models.CharField(max_length=5)
    Start_Date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
    #set up slug automatically
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super().save(*args, **kwargs)



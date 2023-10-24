from django.db import models
#from phonenumber_field.modelfields import *
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class User(models.Model):
    Name=models.CharField(max_length=15)
    Surname=models.CharField(max_length=15)
    Armchair_number=models.CharField(max_length=5)
   # phone_number=PhoneNumberField()
    Start_Date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(unique=True)
    email=models.EmailField(blank=True,null=True)
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
  #  password=models.TextField()
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
    text=models.TextField(null=True)
    #set up slug automatically
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super().save(*args, **kwargs)



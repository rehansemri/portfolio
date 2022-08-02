import email
from email import message
from operator import truediv
from django.contrib.auth.models import User
from django.db import models

class Skills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=200,null=True,blank=True)
    perce = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    bio = models.TextField(null=True,blank=True)
    
    img = models.ImageField(default='img.jpg',upload_to='profile')
    email = models.EmailField(null=True,blank=True)
    mobile = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    def __unicode__(self):
        return self.name

class Qualification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=200,null=True,blank=True)
    college = models.CharField(max_length=200,null=True,blank=True)
    university = models.CharField(max_length=200,null=True,blank=True)
    pass_year = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    title = models.CharField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    img = models.ImageField(default='img.jpg',upload_to='blog')
    def __str__(self):
        return self.title

class Contactus(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=200,null=True)
    message = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
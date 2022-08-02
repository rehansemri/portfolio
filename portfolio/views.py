from email import message
import imp
from django.shortcuts import render
from . models import Blog,Profile,Qualification,Skills,Contactus


def index(request):
    profile = Profile.objects.get(id=1)
    blog = Blog.objects.filter(user = profile.name)
    quali = Qualification.objects.filter(user = profile.name)
    skills = Skills.objects.filter(user = profile.name)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contactus.objects.create(name=name,email=email,subject=subject,message=message)
        contact.save()
    context = { 
        'profile' : profile,
        'blog': blog,
        'quali' : quali,
        'skills': skills,
         }
    return render(request,'index.html',context)


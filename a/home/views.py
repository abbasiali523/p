from django.shortcuts import render
from django.http import HttpResponse
from .models import *



def say_hello(request):
    person={'name':'ali'}
    return render(request,'hello.html',context=person)

def home(request):
    all=Todo.objects.all()
    return render(request,'home.html',{'all':all})

def views_detial(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})

from distutils.log import info
from django.shortcuts import render,redirect
from django.urls import is_valid_path
from .models import *
from .forms import *

def main(request):
    info = sinfo.objects.all()
    #print(info)
    context = {
        'records':info
    }
    return render(request,'crudapp/main.html',context)

def insert_info(request):
    form = SinfoForm

    if request.method == 'POST':
        form = SinfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'crudapp/form.html',context)

def update_info(request,id):
    info = sinfo.objects.get(id=id)
    form  = SinfoForm(instance = info)

    if request.method == 'POST':
        form = SinfoForm(request.POST,instance = info)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'crudapp/form.html',context)

def delete_info(request,id):
    info = sinfo.objects.get(id=id)
    info.delete()
    return redirect('/')
    


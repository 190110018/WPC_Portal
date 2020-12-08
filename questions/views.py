from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm,FileUploadForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import *   

def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for ' + user)
            return redirect('login')

    context={'form':form}
    return render(request,'questions/register.html',context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('instructions')
        else:
            messages.info(request,"Username or Password Incorrect")

    context = {}
    return render(request,'questions/login.html',context)

@login_required(login_url='login')
def instructions(request):
    return render(request,'questions/instructions.html')

@login_required(login_url='login')
def Problem(request):
    
    return render(request,'questions/problems.html')

@login_required(login_url='login')
def upload_file(request):
    user = request.user
    
    form = FileUploadForm({'user':user})
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES,{'user':user})
        if form.is_valid():
            form.save()
            messages.success(request,'File Uploaded')
            return redirect('problems')
    return render(request,'questions/upload_file.html',{'form':form})






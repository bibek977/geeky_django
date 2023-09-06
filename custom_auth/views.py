from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User

def custom_auth(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = UserChangeForm(request.POST ,instance = request.user)
            if fm.is_valid():
                messages.success(request,"Profile updated")
                fm.save()
                return redirect('custom_auth')

        else:
            fm = UserChangeForm(instance = request.user)
            return render(request, 'custom_auth/custom_auth.html',{'form':fm})
    else:
        return redirect("user_login")
    

def user_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = CustomAdminChange(request.POST ,instance = request.user)
                user = User.objects.all()
            else:
                fm = CustomUserChange(request.POST ,instance = request.user)
                user = None
            if fm.is_valid():
                messages.success(request,"Profile updated")
                fm.save()

        if request.user.is_superuser == True:
            fm = CustomAdminChange(instance = request.user)
            user = User.objects.all()
        
        else:
            fm = CustomUserChange(instance = request.user)
            user = None
        return render(request, 'custom_auth/user_change.html',{'form':fm, 'user':user})
    else:
        return redirect("user_login")


def user_detail(request,username):
    if request.user.is_authenticated:
        user_data = User.objects.get(username=username)
        fm = CustomUserChange(instance = user_data)
        if request.method == "POST":
            fm = CustomUserChange(request.POST, instance = user_data)
            if fm.is_valid():
                fm.save()
            return render(request,'custom_auth/user_detail.html',{'form':fm})
        else:
            return render(request,'custom_auth/user_detail.html',{'form':fm})
    else:
         return redirect('user_login')
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import *
from django.contrib import messages

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
        fm = CustomUserChange(instance = request.user)
        return render(request, 'custom_auth/user_change.html',{'form':fm})

    else:
        return redirect("user_login")
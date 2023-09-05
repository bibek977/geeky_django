from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

# def user_creation(request):
#     if request.method == "POST":
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request,'auth_user/user_creation.html',{'form':fm})

def auth_user(request):
    if request.user.is_authenticated:
        return render(request,'auth_user/index.html')
    else:
        return redirect('user_login')

def user_creation(request):
    if request.method == "POST":
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['username']
            fm.save()
            messages.success(request,f"{name} is created")
            return redirect('user_login')
    else:
        fm = SingUpForm()
    return render(request,'auth_user/user_creation.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uid = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uid,password = upass)
                if user is not None:
                    login(request,user)
                    data = {'user':request.user}
                    messages.success(request, f'Welcome {uid}')
                    return redirect('auth_user')
        else:       
            fm = AuthenticationForm()
        return render(request, 'auth_user/user_login.html',{'form':fm})
    else:
        return redirect('auth_user')

def user_logout(request):
    logout(request)
    return redirect("user_login")

def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,request.user)
                messages.success(request,f"{request.user} password changed")
                return redirect('auth_user')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'auth_user/password_change.html',{'form':fm})
    else:
        return redirect('user_login')

def set_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,request.user)
                messages.success(request,f"{request.user} password changed")
                return redirect('auth_user')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request,'auth_user/password_change.html',{'form':fm})
    else:
        return redirect('user_login')
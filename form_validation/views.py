from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

# def form_validation(request):
#     if request.method == "POST":
#         fm = StudentForm(request.POST)
#         if fm.is_valid():
#             return HttpResponseRedirect("/django_forms_submit/success/")
#     else:
#         fm=StudentForm()
#     return render(request,'form_validation/validation.html',{"forms":fm})

def form_validation(request):
    if request.method == "POST":
        fm = StudentTwoForm(request.POST)
        if fm.is_valid():
            return HttpResponseRedirect("/django_forms_submit/success/")
    else:
        fm=StudentTwoForm()
    return render(request,'form_validation/validation.html',{"forms":fm})
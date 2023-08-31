from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect

def django_forms_submit(request):

    if request.method == "POST":
        fm = StudentForm(request.POST)
        # print(fm)
        # print(fm.cleaned_data)
        # print(fm.cleaned_data['name'])
        if fm.is_valid():
            name = fm.cleaned_data['name']
            roll = fm.cleaned_data['roll']
            program = fm.cleaned_data['program']
            print(name,roll,program)

            # return redirect("django_forms_submit")
            # return render(request,"django_forms_submit/response.html",{'name':name})
            return HttpResponseRedirect("/django_forms_submit/success/")
        else:
            print("form is invalid")
    else:
        fm = StudentForm()
    return render(request,'django_forms_submit/index.html',{'forms': fm})

def register(request):
    return render(request,'django_forms_submit/response.html')
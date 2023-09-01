from django.shortcuts import render,redirect
from .forms import *
from .models import *

# def model_form(request):
#     if request.method == "POST":
#         fm = StudentForm(request.POST)
#         if fm.is_valid():
#             n = fm.cleaned_data['name']
#             f = fm.cleaned_data['faculty']
#             r = fm.cleaned_data['roll']
#             st = Student(name=n,faculty=f,roll=r)
#             st.save()

#             return redirect('model_form')
#     else:
#         fm = StudentForm()
#     return render(request,'model_form/index.html',{'form': fm})


def model_form(request):
    if request.method == "POST":
        fm = InternForm(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            p = fm.cleaned_data['program']
            l = fm.cleaned_data['location']
            ph = fm.cleaned_data['phone']

            # st = Intern(id =1,name=n,program=p,location=l, phone=ph)
            # st.save()
            
            # st = Intern(id=1)
            # st.delete()
            
            st = Intern(name=n,program=p,location=l, phone=ph)
            st.save()

            return redirect('model_form')
    else:
        fm = InternForm()
    return render(request,'model_form/index.html',{'form': fm})



# def model_form(request):
#     if request.method == "POST":
#         pi = Intern.objects.get(pk=1)
#         fm = InternForm(request.POST, instance = pi)
#         if fm.is_valid():
#             fm.save()

#             return redirect('model_form')
#     else:
#         fm = InternForm()
#     return render(request,'model_form/index.html',{'form': fm})
from django.shortcuts import render
from .forms import *

def std_forms(request):
    # gives id = id_sid
    # fm = StudentForm()

    # gives id = sid
    # fm = StudentForm(auto_id=True)

    # doesn't give any id
    # fm = StudentForm(auto_id=False)

    # gives bibek_sid
    # fm = StudentForm(auto_id='bibek_%s')

    # fm = StudentForm(auto_id=True,label_suffix="=")
    # fm = StudentForm(auto_id=True,label_suffix="")
    
    fm = StudentForm(auto_id=True,label_suffix="",initial={'sid':161743,'semail':'bhattarai@bibek.com'})
    
    fm.order_fields(field_order=['sid','sname','colz_name'])

    return render(request,'django_forms/forms.html',{'forms':fm})

def new_forms(request):
    fm = StudentForm()
    return render(request,'django_forms/new_forms.html',{'forms':fm})

# def new_forms(request):
#     fm = StudentTwoForm()
#     return render(request,'django_forms/formtwo.html',{'forms':fm})


def new_forms(request):
    fm = StudentThreeForm(initial={'sid':161743})
    return render(request,'django_forms/formthree.html',{'forms':fm})

def new_forms(request):
    fm = StudentFourForm(initial={'sid':161743})
    return render(request,'django_forms/formthree.html',{'forms':fm})
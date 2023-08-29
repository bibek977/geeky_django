from django.shortcuts import render
from .models import *

def student(request):
    student =Student.objects.all()
    return render(request, 'student/index.html',{'std':student})
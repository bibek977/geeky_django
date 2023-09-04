from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['name', 'roll', 'faculty']
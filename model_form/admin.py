from django.contrib import admin
from .models import *

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('name','faculty','roll')

class InternModelAdmin(admin.ModelAdmin):
    list_display =  ['name','program','location','phone']


admin.site.register(Student,StudentModelAdmin)
admin.site.register(Intern,InternModelAdmin)
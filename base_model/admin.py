from django.contrib import admin
from .models import *

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']

class InternModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','program','created_at']
    
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['id','age','created_at']

class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','created_at']

class NewDeveloperModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','created_at','age']

admin.site.register(Student,StudentModelAdmin)
admin.site.register(Intern,InternModelAdmin)
admin.site.register(Person,PersonModelAdmin)
admin.site.register(Developer,DeveloperModelAdmin)
admin.site.register(NewDeveloper,NewDeveloperModelAdmin)
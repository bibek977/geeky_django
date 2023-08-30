from django.contrib import admin
from .models import *

# admin.site.register(Student)

# class StudentAdmin(admin.ModelAdmin):
#     # list_display = ['sid','sname','spass','semail']
#     list_display = ('sid','sname','spass')

# admin.site.register(Student,StudentAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','spass','semail']
    # list_display = ('sid','sname','spass')
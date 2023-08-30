from django.urls import path
from .views import *

urlpatterns = [
    path('',std_forms,name='std_forms'),
    path('new_forms/',new_forms,name='new_forms'),
]

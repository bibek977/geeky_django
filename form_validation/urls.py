from django.urls import path
from .views import *

urlpatterns = [
    path('',form_validation,name="form_validation"),
]

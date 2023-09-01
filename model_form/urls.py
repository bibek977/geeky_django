from django.urls import path
from .views import *

urlpatterns = [
    path("",model_form,name='model_form'),
]

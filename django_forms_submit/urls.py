from django.urls import path
from .views import *

urlpatterns = [
    path('',django_forms_submit,name="django_forms_submit"),
    path('success/',register,name="success"),
]

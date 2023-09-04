from django.urls import path
from .views import *

urlpatterns = [
    path('', django_messages, name='django_messages'),
]

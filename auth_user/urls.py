from django.urls import path
from .views import *

urlpatterns = [
    path('',auth_user,name='auth_user'),
    path('user_creation/',user_creation,name='user_creation'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('password_change/',password_change,name='password_change'),
    path('set_password/',set_password,name='set_password'),
]

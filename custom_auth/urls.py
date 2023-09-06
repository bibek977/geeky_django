from django.urls import path
from .views import *

# urlpatterns = [
#     path('', custom_auth,name="custom_auth" ),
#     path('user_change/', user_change,name="user_change" )
# ]

urlpatterns = [
    path('',custom_auth,name="custom_auth"),
    path('user_change/',user_change,name="user_change"),
    path('user_detail/<str:username>',user_detail,name="user_detail")
]

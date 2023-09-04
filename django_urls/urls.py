from django.urls import path, register_converter
from .views import *
from .converters import *

register_converter(FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('',django_urls,name='django_urls'),
    path('item/<int:id>/',item , {'check' : 'ok'} ,name="item"),
    path('item/<int:id>/<int:sub_id>/', sub_item,name="sub_item"),

    path('custom_year/<yyyy:year>/', custom_year,name='custom_year')
]

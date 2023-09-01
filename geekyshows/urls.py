from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('sample_app/', include('sample_app.urls')),
    path('student',include('student.urls')),
    path('django_forms/', include('django_forms.urls')),
    path('django_forms_submit/', include('django_forms_submit.urls')),
    path('form_validation/',include("form_validation.urls")),
    path('model_form/',include("model_form.urls")),
]

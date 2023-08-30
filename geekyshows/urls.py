from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('sample_app/', include('sample_app.urls')),
    path('student',include('student.urls')),
    path('django_forms/', include('django_forms.urls'))
]

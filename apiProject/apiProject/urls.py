from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentData/', studentData, name='studentData'),
    path('', addStudent, name='addStudent')
]

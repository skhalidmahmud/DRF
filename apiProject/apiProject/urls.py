from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentData/', studentData, name='studentData'),
    path('addStudent/', addStudent, name='addStudent'),
    path('updateStudent/<int:pk>/', updateStudent, name='updateStudent'),
    path('deleteStudent/<int:pk>/', deleteStudent, name='deleteStudent'),

    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),   # GET, POST
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),   # GET, PUT, DELETE
]

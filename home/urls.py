from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', home),
    path('student', post_student),
    path('update-student/<int:id>', update_student)
    
]

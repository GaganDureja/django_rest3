from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('student/', StudentAPI.as_view()),

    path('register/',ResgisterUser.as_view()),

    path('pdf/',GeneratePdf.as_view()),
    path('excel/', ExportImportExcel.as_view()),
    
    path('generic-student/', StudentGeneric.as_view()),
    path('generic-student/<id>', StudentGenericID.as_view()),

    # path('', home),
    # path('student/', post_student),
    # path('update-student/<int:id>', update_student),
    # path('delete-student/<int:id>', delete_student),
    path('book/', get_book)
]

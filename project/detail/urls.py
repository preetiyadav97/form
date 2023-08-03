from django.contrib import admin
from django.urls import path
from .views import Table,Create
urlpatterns = [
    path('first/',Table),
    path('create/',Create,name="cre1")
    
]
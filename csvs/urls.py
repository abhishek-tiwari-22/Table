from django.contrib import admin
from django.urls import path
from .views import *

app_name='csvs'
urlpatterns = [
    path('',file_upload,name='upload csv'),
]
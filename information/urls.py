from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('csv_data/',csv_data),
]

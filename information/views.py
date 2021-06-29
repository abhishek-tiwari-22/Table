from django.shortcuts import render
from .models import *

def csv_data(requests):
    alldata=Info.objects.all()
    context={'data':alldata}
    return render(requests,'table.html',context)

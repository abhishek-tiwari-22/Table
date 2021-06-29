from django.shortcuts import render
from .forms import CsvModelForm
from .models import *
import csv
from information.models import *
# Create your views here.
def file_upload(request):
    form=CsvModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvModelForm()
        obj=Csv.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader=csv.reader(f)
            
            for i,row in enumerate(reader):
                if i!=0:
                    Info.objects.create(
                        Name_of_the_Board=row[0].upper(),
                        appeared_boys=row[1],
                        appeared_girls=row[2],
                        appeared_total=row[3],

                        passed_boys=row[4],
                        passed_girls=row[5],
                        passed_total=row[6],

                        sc_appeared_boys=row[7],
                        sc_appeared_girls=row[8],
                        sc_appeared_total=row[9],

                        sc_passed_boys=row[10],
                        sc_passed_girls=row[11],
                        sc_passed_total=row[12],

                        st_appeared_boys=row[13],
                        st_appeared_girls=row[14],
                        st_appeared_total=row[15],

                        st_passed_boys=row[16],
                        st_passed_girls=row[17],
                        st_passed_total=row[18],
                    )

            obj.activated=True
            obj.save()
    return render(request,'csvs/upload.html',{'form':form})
from .models import *
from django import forms
class CsvModelForm(forms.ModelForm):
    class Meta:
        model=Csv
        fields=('file_name',)
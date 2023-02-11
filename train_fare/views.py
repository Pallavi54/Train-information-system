from django.shortcuts import render
from django.http import HttpResponse
from train_fare.models import fare
from . import forms
from .forms import fare_form

# Create your views here.

def fares(request):
    form = fare_form()
    if request.method == 'POST':
        form = fare_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h2>Record updated successfully</h2>")
    else:
        print("ERROR:form is invalid")
    return render(request,'T_fare/fare.html',context=dict({'form_f':form}))

def fare_report(request):
    fare_list = fare.objects.order_by("train_id")
    fare_dict = {"fare":fare_list}
    return render(request,'T_fare/fare_report.html',context = fare_dict)

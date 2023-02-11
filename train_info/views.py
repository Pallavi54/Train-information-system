from django.shortcuts import render
from django.http import HttpResponse
from train_info.models import train_details
from . import forms
from .forms import train_form

# Create your views here.

def home(request):
    return render(request,'T_info/home.html')
    # return HttpResponse("This is Home page")

def t_info(request):
    form = train_form()
    if request.method == 'POST':
        form = train_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h2>Record updated successfully</h2>")
            # (/'redirect page name'/)
    else:
        print("ERROR:form is invalid")
    return render(request,'T_info/t_info.html',context=dict({'form_d':form}))
    # return HttpResponse("This is Train information page")

def report(request):
    train_list = train_details.objects.order_by("Train_id")
    train_dict = {"train_details":train_list}
    return render(request,'T_info/report.html',context = train_dict)
    # return HttpResponse("This is Report page")

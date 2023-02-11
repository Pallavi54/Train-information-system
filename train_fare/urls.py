from django.urls import path
from train_fare import views

urlpatterns = [
    path('fares',views.fares,name="fares"),
    path('fare_report',views.fare_report,name="fare_report"),
]
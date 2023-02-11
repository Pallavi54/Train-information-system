from django.urls import path
from train_info import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('t_info',views.t_info,name="t_info"),
    path('report',views.report,name="report"),
]
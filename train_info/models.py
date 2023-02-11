from django.db import models

# Create your models here.

class train_details(models.Model):
    Train_id = models.PositiveIntegerField(primary_key=True)
    Train_name = models.CharField(max_length=260,unique=True)
    Origin_city = models.CharField(max_length=260)
    Destination_city = models.CharField(max_length=260)
    Departure_time = models.TimeField()
    Arrival_time = models.TimeField()
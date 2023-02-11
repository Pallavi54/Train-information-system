from django.db import models

# Create your models here.

class fare(models.Model):
    train_id = models.PositiveIntegerField()
    origin_city = models.CharField(max_length=260)
    destination_city = models.CharField(max_length=260)
    train_fare = models.PositiveIntegerField()


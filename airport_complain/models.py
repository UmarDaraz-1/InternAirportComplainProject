from django.db import models

# Create your models here.
class Flight(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    date = models.DateTimeField(max_length=255,auto_now_add=True)
    flight_name = models.CharField(max_length=255)
    flight_no = models.CharField(max_length=255)
    flight_day = models.CharField(max_length=255)
    flight_date = models.DateTimeField(max_length=255,auto_now_add=True)
    flight_cancellation = models.CharField(max_length=255)
    flight_time = models.CharField(max_length=255)
    select = models.CharField(max_length=255)
    objects = models.Manager()

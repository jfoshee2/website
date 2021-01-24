from django.db import models

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    date = models.DateField()

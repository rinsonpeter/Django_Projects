from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PatientProfile(models.Model):
    phonenumber = models.CharField(max_length=12, unique=True)
    bloodgroup = models.CharField(max_length=5)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    user = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.user


class Booking(models.Model):
    doctor = models.CharField(max_length=120)
    date = models.DateField()
    user = models.CharField(max_length=120, unique=True)
    visitingtime = models.DateField(null=True)

    def __str__(self):
        return self.user

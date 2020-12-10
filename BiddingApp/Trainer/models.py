from django.db import models
from Institution.models import Skills
#from django.contrib.auth.models import User


# Create your models here.

class TrainerProfile(models.Model):
    user=models.CharField(max_length=120,unique=True)
    skill=models.ForeignKey(Skills,on_delete=models.CASCADE)
    Age=models.IntegerField()
    experience=models.IntegerField()
    contact=models.IntegerField(default=9999999999)


    def __str__(self):
        return self.name

class Applications(models.Model):
    user=models.CharField(max_length=120)
    skill=models.CharField(max_length=120)
    title=models.CharField(max_length=120)
    choice = (
        ('Applied', 'Applied'), ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected')
    )    
    status=models.CharField(max_length=120,choices=choice,default='Applied')
    Address=models.CharField(max_length=300)

    def __str__(self):
        return self.user



    



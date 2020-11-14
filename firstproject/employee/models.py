from django.db import models


# Create your models here.

# first = request.POST.get("first")
# email = request.POST.get("email")
# username = request.POST.get("username")
# password = request.POST.get("pwd")

class Employee(models.Model):
    first = models.CharField(max_length=120)
    email = models.CharField(max_length=120, unique=True)
    uname = models.CharField(max_length=120, unique=True)
    pwd = models.CharField(max_length=120)
    sal = models.IntegerField(default=5000)

    def __str__(self):
        return self.first


from django.db import models


# Create your models here.
class Student(models.Model):
    stud_email = models.CharField(max_length = 120, unique = True)
    stud_pwd = models.CharField(max_length = 120)

    def __str__(self):
        return self.stud_email

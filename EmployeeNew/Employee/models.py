from django.db import models


# Create your models here.
class ModelDept(models.Model):
    department = models.CharField(max_length = 120, unique = True)

    def __str__(self):
        return self.department
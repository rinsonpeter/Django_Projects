from django.db import models

# Create your models here.

class ModelDept(models.Model):
    department = models.CharField(max_length = 120, unique = True)

    def __str__(self):
        return self.department

class ModelEmpolyee(models.Model):
    emp_id=models.IntegerField(unique=True,blank=False)
    name=models.CharField(max_length=100)       
    dept=models.ForeignKey(ModelDept,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        


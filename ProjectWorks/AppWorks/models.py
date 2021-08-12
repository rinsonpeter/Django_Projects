from django.db import models

# Create your models here.
class ModelProject(models.Model):
    str_project_name=models.CharField(max_length=50,null=False,blank=False,unique=True)
    str_project_code=models.CharField(max_length=50,null=False,blank=False,unique=True)
    int_status=models.IntegerField()

class ModelWorkTypes(models.Model):
    str_worktype_name=models.CharField(max_length=50,null=False,blank=False,unique=True)
    int_order=models.IntegerField()

class=    


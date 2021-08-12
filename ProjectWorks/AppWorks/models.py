from django.db import models
from django.db.models.base import Model

# Create your models here.
class ModelProject(models.Model):
    str_project=models.CharField(max_length=50,null=False,blank=False,unique=True)
    str_project_code=models.CharField(max_length=50,null=False,blank=False,unique=True)
    int_status=models.IntegerField()

    def __str__(self):
        return self.str_project

class ModelWorkTypes(models.Model):
    str_worktype=models.CharField(max_length=50,null=False,blank=False)
    int_order=models.IntegerField()

    def __str__(self):
        return self.str_worktype

class ModelWorkStatus(models.Model):
    str_workstatus=models.CharField(max_length=50,null=False,blank=False)
    str_workstatus_code=models.CharField(max_length=50)
    int_order=models.IntegerField()

    def __str__(self):
        return self.str_workstatus

class ModelWorks(models.Model):
    str_title=models.CharField(max_length=50,null=False, blank=False)
    txt_description=models.TextField(max_length=200)
    fk_project_id=models.ForeignKey(ModelProject,on_delete=models.CASCADE)
    jsn_attachment=models.JSONField(null=True,blank=True)
    dbl_estimatation=models.FloatField(null=True,blank=True)
    dat_start=models.DateField(null=True,blank=True)
    dat_end=models.DateField(null=True,blank=True)
    dat_created=models.DateField(auto_now=True)
    fk_type_id=models.ForeignKey(ModelWorkTypes,on_delete=models.CASCADE)
    dat_approved=models.DateTimeField(null=True,blank=True)
    fk_work_status_id=models.ForeignKey(ModelWorkStatus,on_delete=models.CASCADE)
    dbl_taken=models.FloatField(default=0)
    int_active=models.IntegerField(default=0)

    def _str_(self):
        return self.str_title
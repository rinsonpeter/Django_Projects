from django.db import models

# Create your models here.


class Skills(models.Model):
    skill = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.skill

class Jobs(models.Model):
    skillset=models.ForeignKey(Skills,on_delete=models.CASCADE)
    jobTitle=models.CharField(max_length=120)
    experience=models.IntegerField()
    hourlyRate=models.IntegerField()

    def __str__(self):
        return self.jobTitle

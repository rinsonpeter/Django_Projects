from django.db import models

# Create your models here.

class Order(models.Model):
    mobile=models.CharField(max_length = 120)
    user=models.CharField(max_length = 120)
    quantity=models.IntegerField()
    address=models.CharField(max_length = 200)
    status=models.CharField(max_length = 120,editable = False,default = 'ordered')


    def __str__(self):
        return self.mobile+self.user
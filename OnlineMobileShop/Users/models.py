from django.db import models


# Create your models here.

class Order(models.Model):
    mobile = models.CharField(max_length = 120)
    user = models.CharField(max_length = 120)
    quantity = models.IntegerField()
    address = models.CharField(max_length = 200)
    choice = (
        ('Ordered', 'Ordered'), ('Dispached', 'Dispached'),
        ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')
    )
    status = models.CharField(max_length = 120, default = 'Ordered', choices = choice)

    def __str__(self):
        return self.mobile + self.user

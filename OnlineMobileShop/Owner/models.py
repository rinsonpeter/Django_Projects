from django.db import models


# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length = 120, unique = True)

    def __str__(self):
        return self.brand_name


class Mobile(models.Model):
    mob_name = models.CharField(max_length = 150, unique = True)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    ram = models.CharField(max_length = 50)
    internal = models.CharField(max_length = 120)
    color = models.CharField(max_length = 120)
    screensize = models.CharField(max_length = 120)
    processor = models.CharField(max_length = 120)
    price = models.IntegerField(default = 1500)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.mob_name

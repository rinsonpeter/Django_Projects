from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 120)
    ingredients = models.CharField(max_length = 220)
    category = models.CharField(max_length = 80)

    def __str__(self):
        return self.recipe_name

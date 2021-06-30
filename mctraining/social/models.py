from django.db import models
from django.contrib.auth.models import User

class Profile_model(models.Model):
    profile = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic=models.ImageField(upload_to='images',blank=False)
    phone=models.IntegerField(default=None,null=True)

    def __str__(self):
        return self.profile.username


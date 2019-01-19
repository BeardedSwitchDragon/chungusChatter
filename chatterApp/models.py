from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatterUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    username = models.CharField(max_length=30)
    def __str__(self):
        return self.user.username

    def return_profile_pic():
        return profile_pic

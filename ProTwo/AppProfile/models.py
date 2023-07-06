from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to="profile_pic/")

    def __str__(self):
        return self.user.username

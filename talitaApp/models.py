from distutils.command.upload import upload
from xml.dom.minidom import parseString
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.user



class Image(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='profile_images')
    nameimage = models.CharField(max_length=100)


    def __str__(self):
        return self.nameimage

    
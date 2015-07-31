from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
	dob = models.DateField(blank=True,null=True)
	profile_pic = models.ImageField(upload_to = "profile_pics/",blank = True)
	following = models.ManyToManyField("self",symmetrical=False,related_name="followers")
		



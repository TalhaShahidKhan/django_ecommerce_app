from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import UserManager
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11,blank=True)
    address = models.CharField(max_length=50,blank=True)
    REQUIRED_FIELDS = []
    objects = UserManager()
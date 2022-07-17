from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Users(AbstractUser):
    username = models.CharField(primary_key=True, max_length=30, blank=False)
    password = models.CharField(blank=False, max_length=100)

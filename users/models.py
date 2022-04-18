from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.CharField(max_length=150, null=True, blank=True)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
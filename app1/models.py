from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

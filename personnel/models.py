from django.db import models
from django.contrib.auth.models import AbstractUser

from .definitions import Gender

# Create your models here.


class User(AbstractUser):
    # username_validator
    # username
    # first_name
    # last_name
    ID_number = models.CharField(max_length=15, unique=True, null=False, blank=False)

    # email
    email_verification = models.BooleanField(default=False)

    # is_staff
    # is_active
    # date_joined
    gender = models.PositiveIntegerField(default=Gender.Unset.value[0])
    gender_updated = models.BooleanField(default=False)

    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_verification = models.BooleanField(default=False)

    birthday = models.DateField(null=True, auto_now=False)
    birthday_updated = models.BooleanField(default=False)

    household_address = models.CharField(max_length=200, null=True, blank=True)
    contact_address = models.CharField(max_length=200, null=True, blank=True)

    updated_time = models.DateTimeField(auto_now=True)
    introduction = models.TextField()

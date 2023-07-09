from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from phone_field import PhoneField


class contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    phone = PhoneField(blank=True, help_text='Contact number')
    message = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "{} - {}".format(self.first_name, self.email)
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Announcement(models.Model):
    STATUS = (
        ('DISABLED', 'DISABLED'),
        ('ACTIVE', 'ACTIVE'),
    )
    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    status = models.CharField(max_length=10, choices=STATUS, default='DISABLED')
    
    def __str__(self):
        return "{} - {}".format(self.title, self.creator)
        
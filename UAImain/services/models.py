from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class services(models.Model):
    service_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=255, default='add description')
    description = RichTextField()
    
    def __str__(self):
        return '{}'.format(self.service_name)


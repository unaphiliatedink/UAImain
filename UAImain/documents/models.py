from django.db import models
#from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
from phone_field import PhoneField

# Create your models here.
class documentsBase(models.Model):
    # Document Information
    document_name = models.CharField(max_length=255)
    document_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=255, default='add summary')
    
    # Client Information
    client_name = models.CharField(max_length=255)
    client_date_of_birth = models.DateField()
    client_address = models.CharField(max_length=255, default='add address')
    client_phone = PhoneField(blank=True, help_text='Contact number')
    client_email = models.EmailField(max_length=60)
    client_emergency_contact = models.CharField(max_length=255)
    client_drivers_license = models.CharField(max_length=50)
    
    # Health information
    allergies = models.CharField(max_length=200, blank=True)
    medical_conditions = models.CharField(max_length=200, blank=True)
    medications = models.CharField(max_length=200, blank=True)
    pregnancy = models.BooleanField(default=False)
    skin_conditions = models.CharField(max_length=200, blank=True)
    
    # Consent
    consent_terms = models.BooleanField(default=False)
    date_signed = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True
        ordering = ['created']
    
    def __str__(self):
        return '{}'.format(self.document_name)
        
class body_art_consent(documentsBase):  
    # Tattoo information
    tattoo_design = models.CharField(max_length=100)
    tattoo_placement = models.CharField(max_length=100)
    tattoo_size = models.CharField(max_length=100)
    #consent = RichTextField()
    
    def __str__(self):
        return self.client_name

class tattoo_consent(models.Model):  
    # Document Information
    document_name = models.CharField(max_length=255)
    document_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # Document
    consent = RichTextField()
    
    def __str__(self):
        return self.document_name
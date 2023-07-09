from django.contrib import admin
from .models import *

# Register your models here.

class tattoo_consentAdmin(admin.ModelAdmin):
    pass
admin.site.register(tattoo_consent, tattoo_consentAdmin)
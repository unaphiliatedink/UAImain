from django.contrib import admin
from services.models import *

# Register your models here.

class servicesAdmin(admin.ModelAdmin):
    pass
admin.site.register(services, servicesAdmin)

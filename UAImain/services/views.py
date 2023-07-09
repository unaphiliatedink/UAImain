from django.shortcuts import render
from django.views import View
from .models import services

# Create your views here.
class servicesIndex(View):
    def get(self, request, *args, **kwargs):
        service_items = services.objects.all()
        context = {
                'service_items': service_items,
        }
        
        return render(request, 'services/services_index.html', context)

    def post(self, request, *args, **kwargs):
        service_items = services.objects.all()
        context = {
                'service_items': service_items,
        }
        
        return render(request, 'services/services_index.html', context)
        
class Piercings(View):
    def get(self, request, *args, **kwargs):
        piercing = services.objects.all().filter(service_name='Piercings')
        
        context = {
                'piercing': piercing,
        }
        return render(request, 'services/piercings.html', context)  
        
class Tattoos(View):
    def get(self, request, *args, **kwargs):
        tattoo = services.objects.all().filter(service_name='Tattoo')
        
        context = {
                'tattoo': tattoo,
        }
        return render(request, 'services/tattoos.html', context)  
        
class Microblading(View):
    def get(self, request, *args, **kwargs):
        microblading = services.objects.all().filter(service_name='Micro-blading')
        
        context = {
                'microblading': microblading,
        }
        return render(request, 'services/micro-blading.html', context)  

class Pmu(View):
    def get(self, request, *args, **kwargs):
        pmu = services.objects.all().filter(service_name='Permanent Make Up')
        
        context = {
                'pmu': pmu,
        }
        return render(request, 'services/pmu.html', context)
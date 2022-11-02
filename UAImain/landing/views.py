from django.shortcuts import render
from django.views import View




class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
        
        
class contactPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/baseContact.html')        
 
#class contactPageView(View):
#    template_name = 'landing/baseContact.html'    
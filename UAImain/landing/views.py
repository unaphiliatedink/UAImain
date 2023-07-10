from django.shortcuts import render
from django.views import View
from dashboard.models import Announcement


class Index(View):
    def get(self, request, *args, **kwargs):
        announce_message = Announcement.objects.all().order_by('-created_on')
        
        context = {
            'announce': announce_message,
        }
        
    
        return render(request, 'landing/index.html', context)
        
 


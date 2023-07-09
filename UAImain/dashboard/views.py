from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import View
from .models import Announcement
from contact.models import contact
from .forms import announcementForm

class dashHome(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        announce_message = Announcement.objects.all().order_by('-created_on')
        contact_leads = contact.objects.all().order_by('-created_on')
        form = announcementForm()
        
        context = {
            'announce': announce_message,
            'contact_leads': contact_leads,
            'form': form,
        }
        
        return render(request, 'dashboard/dash_home.html', context)

    def post(self, request, *args, **kwargs):
        announce_message = Announcement.objects.all().order_by('-created_on')
        contact_leads = contact.objects.all().order_by('-created_on')
        form = announcementForm(request.POST)
        
        if form.is_valid():
            new_announcement = form.save(commit=False)
            new_announcement.creator = request.user
            new_announcement.save()
        
        context = {
            'announce': announce_message,
            'contact_leads': contact_leads,
            'form': form,
        }
        
        return render(request, 'dashboard/dash_home.html', context)


class announcementDetail(LoginRequiredMixin, DetailView):
    model = Announcement
    template_name = 'dashboard/announcement_detail.html'
    

class announcementUpdate(LoginRequiredMixin, UpdateView):
    model = Announcement
    fields = [        
        "creator",
        "created_on",
        "title",
        "message",
        "status"
    ]
    template_name_suffix = '_detail_update_form'
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/dashboard"
    

        # return self.request.user == post.author
        
class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = '/dashboard'
    
    template_name = 'dashboard/announcement_confirm_delete.html'
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from django.views import View
from .models import contact
from .forms import contactForm
from django.contrib import messages
from sms import send_sms

class contactPageView(View):
    def get(self, request, *args, **kwargs):
        contact_us = contact.objects.all().order_by('-created_on')
        form = contactForm()
        
        context = {
            'contact_us': contact_us,
            'form': form,
        }
        
        return render(request, 'contact/baseContact.html', context)

    def post(self, request, *args, **kwargs):
        contact_us = contact.objects.all().order_by('-created_on')
        form = contactForm(request.POST)
        
        if form.is_valid():
            new_contact = form.save(commit=False)
            #new_contact_us.creator = request.user
            new_contact.save()
        
        context = {
            'contact_us': contact_us,
            'form': form,
        }
        
        return render(request, 'contact/baseContact.html', context)


  
def contact_form(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            
            return render(request, 'contact/contact_form.html', {'form': contactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = contactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
  

class contactDetail(LoginRequiredMixin, DetailView):
    model = contact
    success_url = '/dashboard/'
    template_name = 'contact/contact_detail.html'
    
    
class contactSuccessful(DetailView):
    model = contact
    template_name = 'contact/contact_successful.html'

class contactDeleteView(LoginRequiredMixin, DeleteView):
    model = contact
    success_url = '/'
    
    template_name = 'contact/contact_confirm_delete.html'
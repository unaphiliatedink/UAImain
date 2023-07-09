from django.shortcuts import render, redirect
from django.views import View
#from .models import documents
from .forms import TattooConsentForm

# Create your views here. 
class documentsIndex(View):
    def get(self, request, *args, **kwargs):
        
        context = {
        
        }
        
        return render(request, 'documents/documents_index.html', context)

    def post(self, request, *args, **kwargs):
        
        context = {
        
        }
        
        return render(request, 'documents/documents_index.html', context)
    

def consent_form(request):
    if request.method == 'POST':
        form = TattooConsentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TattooConsentForm()
    return render(request, 'documents/consent_form.html', {'form': form})

def success(request):
    return render(request, 'documents/success.html')


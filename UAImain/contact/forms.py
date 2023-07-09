from django import forms
from .models import contact

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'created_on']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'created_on': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

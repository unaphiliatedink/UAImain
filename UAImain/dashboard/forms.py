from django import forms
from .models import Announcement

class announcementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['creator', 'created_on', 'title', 'message', 'status']
        
        widgets = {
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'created_on': forms.DateTimeInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

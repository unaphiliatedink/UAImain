from django import forms
from .models import body_art_consent

class TattooConsentForm(forms.ModelForm):
    class Meta:
        model = body_art_consent
        exclude = ['date_signed']

    def clean(self):
        cleaned_data = super().clean()

        # Check if the user is over 18 years old
        date_of_birth = cleaned_data.get('client_date_of_birth')
        if date_of_birth:
            age = (date.today() - date_of_birth).days // 365
            if age < 18:
                raise forms.ValidationError('You must be 18 years or older to get a tattoo.')

        # Check if the user has agreed to the consent terms
        consent_terms = cleaned_data.get('consent_terms')
        if not consent_terms:
            raise forms.ValidationError('You must agree to the consent terms to get a tattoo.')

        return cleaned_data

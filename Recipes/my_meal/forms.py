from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    
        fields = [
                'profile_pic', 'diet_preference', 'gender', 'bio', 
                'date_of_birth', 'location', 'website', 'social_media', 'phone_number','weight','health_goals',
            ]  # ✅ Ensure fields are specified correctly

        widgets = {
                'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'location': forms.TextInput(attrs={'class': 'form-control'}),
                'website': forms.URLInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            }
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class GetChefForm(forms.Form):
    live_location = forms.URLField(label="Live Location (Google Maps Link)", required=True)
    reason = forms.CharField(label="Reason for Chef", widget=forms.Textarea, required=True)
    event_size = forms.IntegerField(label="How big is the event?", required=True)
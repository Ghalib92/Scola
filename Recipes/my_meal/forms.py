from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    
        fields = [
                'profile_pic', 'diet_preference', 'gender', 'bio', 
                'date_of_birth', 'location', 'website', 'social_media', 'phone_number'
            ]  # ✅ Ensure fields are specified correctly

        widgets = {
                'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'location': forms.TextInput(attrs={'class': 'form-control'}),
                'website': forms.URLInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            }
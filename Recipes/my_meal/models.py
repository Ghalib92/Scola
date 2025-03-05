from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')  # Stores images in /media/blog_images/

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User  # Django's built-in user model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('allergic', 'Allergic'),
        ('diabetic', 'Diabetic'),
        ('normal', 'No Restrictions'),
        
    ]
    
    diet_preference = models.CharField(max_length=50, choices=DIET_CHOICES, default='normal')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
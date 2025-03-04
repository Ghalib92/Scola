from django.apps import AppConfig


class MyMealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_meal'

from django.contrib.auth.models import User  # Django's built-in user model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  
    diet_preference = models.CharField(
        max_length=50,
        choices=[
            ('vegetarian', 'Vegetarian'),
            ('allergic', 'Allergic'),
            ('diabetic', 'Diabetic'),
            ('normal', 'No Restrictions'),
        ],
        default='normal'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
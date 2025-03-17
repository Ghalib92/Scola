from django.db import models
from django.contrib.auth.models import User


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
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')  # Default is 'Male'
    bio = models.CharField(max_length=150,null=True, blank=True)
    date_of_birth = models.DateField (null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

    
class RecipeBase(models.Model):
    FOOD_TIMES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    
    food_name = models.CharField(max_length=255)
    health_benefits = models.TextField()  # Stored as a comma-separated list
    cooking_procedure = models.TextField()  # Stored as a comma-separated list
    how_to_serve = models.TextField()
    meal_time = models.CharField(max_length=10, choices=FOOD_TIMES)
    meal_image = models.ImageField(upload_to='meal_images/', null=True, blank=True)
   
    class Meta:
        abstract = True  # This ensures that it's not created as a separate table

    def get_health_benefits_list(self):
        return self.health_benefits.split(',')

    def get_cooking_procedure_list(self):
        return self.cooking_procedure.split(',')

    def __str__(self):
        return self.food_name

# Specific Recipe Models for Different Diet Categories
class NormalRecipe(RecipeBase):
    pass

class VegetarianRecipe(RecipeBase):
    pass

class DiabeticRecipe(RecipeBase):
    pass

class AllergicRecipe(RecipeBase):
    pass
class Drinks (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='drink_images/')

    class Meta:
        abstract = True

    def __str__(self):
        return super().__str__()
class AllergicDrinks(Drinks):
    pass
class DiabeticDrinks(Drinks):
    pass  
class VegeterianDrinks(Drinks):
    pass


class NormalDrinks(Drinks):
    pass


class Snacks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='snack_images/')

    class Meta:
        abstract = True

        def __str__(self):
            return super().__str__()
 
class AllergicSnacks(Snacks):
    pass
class DiabeticSnacks(Snacks):
    pass  
class VegeterianSnacks(Snacks):
    pass

class NormalSnacks(Snacks):
    pass
 
class Desserts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='snack_images/')

    class Meta:
        abstract = True

        def __str__(self):
            return super().__str__()
class AllergicDesserts(Desserts):
    pass
class DiabeticDesserts(Desserts):
    pass  
class VegeterianDesserts(Desserts):
    pass

class NormalDesserts(Desserts):
    pass

class Fruits(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='snack_images/')

    class Meta:
        abstract = True

        def __str__(self):
            return super().__str__()
 
class AllergicFruits(Fruits):
    pass
class DiabeticFruits(Fruits):
    pass  
class VegeterianFruits(Fruits):
    pass

class NormalFruits(Fruits):
    pass

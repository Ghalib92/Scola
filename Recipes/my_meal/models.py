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
    GOALS = [
      ('weight_increase','Weight_Increase'),
       ('weight_loss','Weight_Loss'),
      ( 'weight_retantion','Weight_Retantion'),

   ]
    health_goals = models.CharField(max_length=50, choices = GOALS, default='normal'  )
  
    weight = models.IntegerField(null=True, blank=True)
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

 
DIET_CHOICES = [
    ('allergic', 'Allergic'),
    ('diabetic', 'Diabetic'),
    ('vegetarian', 'Vegetarian'),
    ('normal', 'No Restrictions'),
]

class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='drink_images/')
    category = models.CharField(max_length=20, choices=DIET_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Snack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='snack_images/')
    category = models.CharField(max_length=20, choices=DIET_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Dessert(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='dessert_images/')
    category = models.CharField(max_length=20, choices=DIET_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Fruit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='fruit_images/')
    category = models.CharField(max_length=20, choices=DIET_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


# Categories for Weight Management
 
GOALS = [
      ('weight_increase','Weight_Increase'),
       ('weight_loss','Weight_Loss'),
      ( 'weight_retantion','Weight_Retantion'),

   ]

class WeightManagementFood(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='weight_foods/')
    category = models.CharField(max_length=20, choices=GOALS)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class HealthHabits(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='health_habits/')
    category = models.CharField(max_length=20, choices=GOALS ,default='Weight_Retantion')

    def __str__(self):
        return f"{self.name} ({self.description()})"
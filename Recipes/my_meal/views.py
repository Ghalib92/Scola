from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django .contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog

from .forms import ProfileUpdateForm
from .models import UserProfile

# Create your views here.
def home (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home_page')  # Redirect to homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'login.html')

 


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']   
        last_name = request.POST['last_name'] 
        username = request.POST['username'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']  # Fixed the typo
        email = request.POST['email']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')  # Redirect back to the signup page

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'signup.html')  # Show signup form if request is not POST
def logout(request):
    auth.logout(request)
    return redirect('login') 

@login_required(login_url='login') 
def home_page(request):
    return render(request, 'home.html')  # Show home page with user information if logged in

def blog (request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})  # Pass blogs to the template

def about (request):
    return render(request, 'about.html')  # Show about page with information about the website
    

from .forms import ProfileUpdateForm
from .models import UserProfile

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect after saving
    else:
        form = ProfileUpdateForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})
 




def get_meal_suggestion(user):
    """Pick a random meal based on user diet preference and current meal time"""
    user_profile = user.userprofile

    # Determine the current meal time
    current_hour = now().hour
    if current_hour < 10:
        meal_time = 'breakfast'
    elif current_hour < 16:
        meal_time = 'lunch'
    else:
        meal_time = 'dinner'


from django.shortcuts import render
from django.utils.timezone import now
from django.utils.timezone import localtime, now
from .models import AllergicRecipe, VegetarianRecipe, DiabeticRecipe, NormalRecipe

def get_meal_suggestion(user):
    """Pick a random meal based on user diet preference and current meal time"""
    user_profile = user.userprofile

    # Determine the current meal time
    current_hour = localtime(now()).hour 
    if current_hour < 10:
        meal_time = 'breakfast'
    elif current_hour < 16:
        meal_time = 'lunch'
    else:
        meal_time = 'dinner'

    # Select the appropriate meal category
    if user_profile.diet_preference == "allergic":
        qs = AllergicRecipe.objects.filter(meal_time=meal_time)
    elif user_profile.diet_preference == "vegetarian":
        qs = VegetarianRecipe.objects.filter(meal_time=meal_time)
    elif user_profile.diet_preference == "diabetic":
        qs = DiabeticRecipe.objects.filter(meal_time=meal_time)
    else:
        qs = NormalRecipe.objects.filter(meal_time=meal_time)

    # Return a random recipe if available
    if qs.exists():
        return qs.order_by('?').first()
    else:
        return None

def meal_suggestion(request):
    """View to handle meal request"""
    meal = None
    if request.method == "POST":  # If user clicks the button
        meal = get_meal_suggestion(request.user)

    return render(request, 'meal_suggestion.html', {'meal': meal})

from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django .contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog,WeightManagementFood,HealthHabits

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
def update(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect after saving
    else:
        form = ProfileUpdateForm(instance=user_profile)

    return render(request, 'update.html', {'form': form, 'user_profile': user_profile})
 



 


from django.shortcuts import render
from django.utils.timezone import now
from django.utils.timezone import localtime, now
from .models import AllergicRecipe, VegetarianRecipe, DiabeticRecipe, NormalRecipe

def get_meal_suggestion(user):
     import random
from django.utils.timezone import localtime, now

def get_meal_suggestion(user):
    """Pick three random meals (breakfast, lunch, and dinner) based on user diet preference."""
    user_profile = user.userprofile

    # Dictionary to hold meal suggestions
    daily_meals = {
        'breakfast': None,
        'lunch': None,
        'dinner': None
    }

    # Select the appropriate meal category
    if user_profile.diet_preference == "allergic":
        meal_model = AllergicRecipe
    elif user_profile.diet_preference == "vegetarian":
        meal_model = VegetarianRecipe
    elif user_profile.diet_preference == "diabetic":
        meal_model = DiabeticRecipe
    else:
        meal_model = NormalRecipe

    # Fetch meals for each meal time
    for meal_time in daily_meals.keys():
        qs = meal_model.objects.filter(meal_time=meal_time)
        if qs.exists():
            daily_meals[meal_time] = qs.order_by('?').first()

    return daily_meals


def meal_suggestion(request):
    """View to handle meal request."""
    meals = None  # Initialize meals as None

    if request.method == "POST":  # If user clicks the button
        meals = get_meal_suggestion(request.user)

    return render(request, 'meal_suggestion.html', {'meals': meals})
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def drinks(request):
    return render(request, 'drinks.html')

def fruits(request):
    return render(request, 'fruits.html')

def health_habits(request):
    return render(request, 'health_habits.html')

def snacks(request):
    return render(request, 'snacks.html')

def desserts(request):
    return render(request, 'desserts.html')
@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    return render(request, 'profile.html', {'user_profile': user_profile})



from .models import Drink, Snack, Dessert, Fruit, UserProfile
from django.contrib.auth.decorators import login_required


@login_required
def fruit_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommended_fruits = Fruit.objects.filter(category=user_profile.diet_preference)

    return render(request, 'fruits.html', {'recommended_fruits': recommended_fruits})


@login_required
def drinks_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommended_drinks = Drink.objects.filter(category=user_profile.diet_preference)

    return render(request, 'drinks.html', {'recommended_drinks': recommended_drinks})


@login_required
def snacks_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommended_snacks = Snack.objects.filter(category=user_profile.diet_preference)

    return render(request, 'snacks.html', {'recommended_snacks': recommended_snacks})


@login_required
def desserts_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommended_desserts = Dessert.objects.filter(category=user_profile.diet_preference)

    return render(request, 'desserts.html', {'recommended_desserts': recommended_desserts})


@login_required
def weight_management(request):
  
    user_profile = UserProfile.objects.get(user = request.user)  # Ensure user profile exists

    recommended_meals = WeightManagementFood.objects.filter(category = user_profile.health_goals)

    return render(request, 'weight_management.html', {
        'user_profile': user_profile,
        'recommended_meals': recommended_meals
    })

@login_required
def health_habits(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommended_habits = HealthHabits.objects.filter(category=user_profile.health_goals)

    return render(request, 'health_habits.html', {
        'user_profile': user_profile,
        'recommended_habits': recommended_habits
    })



from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose email content
            email_subject = f"Contact Us Form: {subject}"
            email_message = f"Message from: {name} ({email})\n\n{message}"

            # Send email
            try:
                send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
                return HttpResponse('Thank you for your message! We will get back to you soon.')
            except Exception as e:
                return HttpResponse(f'Error: {str(e)}')

    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})
from .forms import GetChefForm
from django.http import HttpResponse

def get_chef_request(request):
    if request.method == 'POST':
        form = GetChefForm(request.POST)
        if form.is_valid():
            # Get form data
            live_location = form.cleaned_data['live_location']
            reason = form.cleaned_data['reason']
            event_size = form.cleaned_data['event_size']

            # Check if user is authenticated
            if request.user.is_authenticated:
                user_email = request.user.email
                user_name = request.user.get_full_name() or request.user.username
            else:
                return HttpResponse("You must be logged in to request a chef.")

            # Email details
            subject = "Chef Request Received"
            message = (
                f"Hello {user_name},\n\n"
                f"Your request for a chef has been received and is being processed.\n\n"
                f"Details:\n"
                f"- Live Location: {live_location}\n"
                f"- Reason: {reason}\n"
                f"- Event Size: {event_size} people\n\n"
                f"A chef will be assigned to you shortly.\n\n"
                f"Thank you for choosing our service!"
            )

            # Send email to user
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])
                return HttpResponse('Your request has been received. Check your email for confirmation.')
            except Exception as e:
                return HttpResponse(f'Error: {str(e)}')

    else:
        form = GetChefForm()

    return render(request, 'get_chef.html', {'form': form})
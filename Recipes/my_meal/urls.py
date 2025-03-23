from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout', views.logout, name='logout'),
    path('home',views.home_page,name='home_page'),
    path('blog',views.blog,name = 'blog'),
    path('about',views.about, name='about'),
    path('profile',views.profile,name = 'profile'),
    path('meal-suggestion', views.meal_suggestion, name='meal_suggestion'),
    path('health-habits/', views.health_habits, name='health_habits'),
    path('update/',views.update,name = 'update'),
    path('drinks/', views.drinks_page, name='drinks'),
    path('snacks/', views.snacks_page, name='snacks'),
    path('desserts/', views.desserts_page, name='desserts'),
    path('fruits/', views.fruits_page, name='fruits'),

]
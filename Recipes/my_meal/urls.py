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
    
]
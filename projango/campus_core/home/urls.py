from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

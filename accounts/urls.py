from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
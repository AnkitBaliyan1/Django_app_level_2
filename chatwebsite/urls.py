
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.home, name='home'),
    path('about/', views.about, name="about"),

]


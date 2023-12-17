
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('translate/', views.translate, name="translate"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('upcoming/', views.upcoming, name="upcoming"),
    path('contactus/', views.contactus, name="contactus"),
]


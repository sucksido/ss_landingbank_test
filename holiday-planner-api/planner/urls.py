# planner/urls.py

from django.urls import path
from .views import WeatherAPIView  # Ensure this import exists and is correct

urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),
]
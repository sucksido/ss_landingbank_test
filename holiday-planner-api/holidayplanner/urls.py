# holidayplanner/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('planner.urls')),  # This should include the URLs from the planner app
]
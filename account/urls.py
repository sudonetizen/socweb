from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]


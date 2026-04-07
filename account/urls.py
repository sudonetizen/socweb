from django.urls import path, include
from .views import dashboard, UserRegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register/', UserRegisterView.as_view(), name='register'),
]


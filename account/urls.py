from django.urls import path, include
from .views import dashboard, UserRegisterView, UserEditView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/', UserEditView.as_view(), name='edit'),
]


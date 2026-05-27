from django.urls import path, include
from .views import dashboard, UserRegisterView, UserEditView, user_list, user_detail, user_follow

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/', UserEditView.as_view(), name='edit'),
    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>/', user_detail, name='user_detail'),
]


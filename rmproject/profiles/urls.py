from django.urls import path
from .views import RegisterUserView, UserProfileListCreateView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profiles/', UserProfileListCreateView.as_view(), name='user-profiles'),
]

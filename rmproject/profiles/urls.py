from django.urls import path
from .views import RegisterUserView, UserProfileDetailAPIView
from .views import CreateUserProfileView, ListUserProfilesView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    # path('profiles/', UserProfileListCreateView.as_view(), name='user-profiles'),
    path('profiles/', CreateUserProfileView.as_view(), name='create-profile'),
    path("profiles/<uuid:guid>/", UserProfileDetailAPIView.as_view(), name="profile-detail"),
    path('profiles/list/', ListUserProfilesView.as_view(), name='list-profiles'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

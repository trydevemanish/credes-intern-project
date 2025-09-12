from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # for admin
    path('users/',view=views.GetUsers.as_view()),
    path('users/<int:id>/soft-delete/',view=views.SoftDeleteaUser.as_view()), # soft deleting a user
    
    # for register user 
    path('auth/register/',view=views.RegisterUser.as_view()),

    # for auth
    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
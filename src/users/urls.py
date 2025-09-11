from django.urls import path
from . import views

urlpatterns = [
    # for admin
    path('users/',view=views.GetUsers),
    path('users/<int:user_id>/soft-delete/',view=views.SoftDeleteaUser), # soft deleting a user
    
    # for user 
    path('auth/register/',view=views.RegisterUser),
    path('auth/login/',view=views.LoginUser),
]
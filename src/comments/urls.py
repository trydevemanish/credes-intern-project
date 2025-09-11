from django.urls import path
from . import views

urlpatterns = [
    #for role -> admin
    path('all/',view=views.FetchCommentsOfTask), #Admin fetches the comment of the tasks

    #for role -> user
    path('',view=views.GetYourComment), # get the comment u add to the task u r assigned
    path('add/',view=views.AddComment), # Add comment to a task assigned to me
]
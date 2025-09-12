from django.urls import path
from . import views

urlpatterns = [
    #for role -> admin
    path('all/',view=views.FetchCommentsOfTask.as_view()), #Admin fetches the comment of the tasks.

    #for role -> user
    path('',view=views.GetYourComment.as_view()), # get the comment that u added to the task u r assigned
    path('add/',view=views.AddComment.as_view()), # Add comment to a task assigned to me
]
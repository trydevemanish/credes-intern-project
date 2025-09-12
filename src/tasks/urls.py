from django.urls import path
from . import views

urlpatterns = [
    #for role -> admin
    path('create/',view=views.CreateTask.as_view(),name='create-task'), #create task
    path('all/',view=views.FetchAllTasks.as_view(),name='fetch-all-tasks'), #fetch all tasks 
    path('<int:id>/delete/', view=views.DeleteTask.as_view()), #delete task
    path('<int:id>/update/', view=views.UpdateTask.as_view()), #update task 


    #for role -> user
    path('',view=views.FetchTask.as_view(),name='fetch-my-tasks'), # fetch all the task assigned to me
    path('<int:id>/',view=views.GetTask.as_view()), # fetch task detail assigned to me with task id
    path('<int:id>/status/',view=views.UpdateStatus.as_view()), # update task status assigned to me with task id
]
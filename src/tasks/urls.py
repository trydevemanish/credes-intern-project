from django.urls import path
from . import views

urlpatterns = [
    #for role -> admin
    path('create/',view=views.CreateTask,name='create-task'), #create task
    path('all/',view=views.FetchAllTasks,name='fetch-all-tasks'), #fetch all tasks 
    path('<int:id>/delete/', view=views.DeleteTask), #delete task
    path('<int:id>/update/', view=views.UpdateTask), #update task 

    #for role -> user
    path('',view=views.FetchTask,name='fetch-my-tasks'), # fetch all the task assigned to me
    path('<int:id>/',view=views.GetTask), # fetch task detail assigned to me with task id
    path('<int:id>/status/',view=views.UpdateStatus), # update task status assigned to me with task id
]
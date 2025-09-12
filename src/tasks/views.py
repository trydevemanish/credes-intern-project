from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.contrib.auth import get_user_model
from utils.permissions import IsAdmin


# Create your views here.
# for role -> admin

class CreateTask(APIView):
    permission_classes = [IsAdmin]
    def post(self,request):
        # serialisedTaskData = 
        pass



def FetchAllTasks():
    pass


def DeleteTask():
    pass


def UpdateTask():
    pass

# for role -> user 

def FetchTask():
    pass


def GetTask():
    pass


def UpdateStatus():
    pass

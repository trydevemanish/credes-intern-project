from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from utils.permissions import IsAdmin,IsActiveUser,IsTaskAssignedToMeOrAdmin
from .serializers import TaskSerializers
from .models import Task

# Create your views here.
# for role -> admin

class CreateTask(APIView):
    permission_classes = [IsAdmin]

    def post(self,request,*args, **kwargs):
        serialisedTaskData = TaskSerializers(data=request.data)
        if serialisedTaskData.is_valid():
            serialisedTaskData.save()
            return Response({'message':'Task created.','data':serialisedTaskData.data},status=status.HTTP_201_CREATED)
        return Response(serialisedTaskData.errors,status=status.HTTP_400_BAD_REQUEST)
      


class FetchAllTasks(APIView):
    permission_classes = [IsAdmin]

    def get(self,request):
        allTasks = Task.objects.all()
        serialisedTasksData = TaskSerializers(allTasks,many=True)
        if not allTasks:
            return Response({'message':'No taks yet.'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message':'Fetched all tasks.','data':serialisedTasksData.data},status=status.HTTP_200_OK)


class DeleteTask(APIView):
    permission_classes = [IsAdmin]

    def delete(self,request,id,*args, **kwargs):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        task.delete()
        return Response({'message':'Task deleted.'},status=status.HTTP_204_NO_CONTENT)


class UpdateTask(APIView):
    permission_classes = [IsAdmin]

    def put(self,request,id,*args, **kwargs):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        serialisedTaskData = TaskSerializers(task,data=request.data,parTial=True)
        if serialisedTaskData.is_valid():
            serialisedTaskData.save()
            return Response({'message':'Task updated.','data':serialisedTaskData.data},status=status.HTTP_200_OK)
        
        return Response(serialisedTaskData.error_messages,status=status.HTTP_400_BAD_REQUEST)


        

# for role -> user 

class FetchTask(APIView):
    permission_classes = [IsActiveUser]

    def get(self,request):
        id=request.user.id # find how to get the user id from the token
        allTaskAssignedtoMe = Task.objects.filter(assigned_to=id).all()

        if not allTaskAssignedtoMe:
            return Response.json({'message':'No task assigned to you'},status=status.HTTP_400_BAD_REQUEST)
        
        serialisedTaskData = TaskSerializers(allTaskAssignedtoMe,many=True)

        return Response({'message':'Tasks assigned to you!','data':serialisedTaskData.data},status=status.HTTP_200_OK)


class GetTask(APIView):
    permission_classes = [IsActiveUser,IsTaskAssignedToMeOrAdmin]

    def get(self,request,id,*args, **kwargs):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        self.check_object_permissions(request=request,obj=task)

        serialisedTaskData = TaskSerializers(task)

        return Response({'message':f'Task found with id:{id}','data':serialisedTaskData.data},status=status.HTTP_200_OK)


class UpdateTaskStatus(APIView):
    permission_classes = [IsActiveUser,IsTaskAssignedToMeOrAdmin]

    def put(self,request,id,*args, **kwargs):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        self.check_object_permissions(request=request,obj=task)

        serialisedTaskData = TaskSerializers(task,data=request.data,parTial=True)
        if serialisedTaskData.is_valid():
            serialisedTaskData.save()
            return Response({'message':'Task updated.','data':serialisedTaskData.data},status=status.HTTP_200_OK)
        
        return Response(serialisedTaskData.error_messages,status=status.HTTP_400_BAD_REQUEST)




        

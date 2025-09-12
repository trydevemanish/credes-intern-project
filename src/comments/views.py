from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from utils.permissions import IsAdmin,IsActiveUser,IsTaskAssignedToMeOrAdmin
from .models import Comment
from .serializers import CommentSerializers
from tasks.models import Task


# Create your views here.

class FetchCommentsOfTask(APIView):
    permission_classes = [IsAdmin]

    def get(self,request,id,*args, **kwargs):
        comments = Comment.objects.filter(task=id).all()
        if not comments:
            return Response({'message':'No comments yet'},status=status.HTTP_400_BAD_REQUEST)
        
        serialisedCommentData = CommentSerializers(comments,many=True)

        return Response({'message':f'Comments on tasks with taskid:{id}.','data':serialisedCommentData.data},status=status.HTTP_200_OK)
    


class GetYourComment(APIView):
    permission_classes = [IsActiveUser,IsTaskAssignedToMeOrAdmin]

    def get(self,request,id,*args, **kwargs):
        task = Task.objects.get(id=id)
        if not task:
                return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        self.check_object_permissions(request=request,obj=task)

        comments = Comment.objects.filter(task=id).all()
        
        if not comments:
            return Response({'message':'No comments added to this tasks.'},status=status.HTTP_200_OK)
        
        commentSerialisedData = CommentSerializers(comments,many=True)

        return Response({'message':'Your comments you added to the tasks.','data':commentSerialisedData.data},status=status.HTTP_200_OK)

        



class AddComment(APIView):
    permission_classes = [IsActiveUser,IsTaskAssignedToMeOrAdmin]

    def post(self,request,id,*args, **kwargs):
        task = Task.objects.get(id=id)
        if not task:
                return Response({'message':'Invalid task id.'},status=status.HTTP_400_BAD_REQUEST)
        
        self.check_object_permissions(request=request,obj=task)

        newSerialisedComment = CommentSerializers(data=request.data)

        if newSerialisedComment.is_valid():
            newSerialisedComment.save()
            return Response({'message':f'Comment created on task id:{id}.','data':newSerialisedComment.data},status=status.HTTP_201_CREATED)
        
        return Response(newSerialisedComment.errors,status=status.HTTP_400_BAD_REQUEST)

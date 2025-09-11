from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializers,UserTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.permissions import IsAdmin

User = get_user_model()

# Create your views here.

class RegisterUser(APIView):

    def post(self,request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            checkUserExit = User.objects.filter(email=email).exists()
            if checkUserExit:
                print('Email already exits!')
                return Response({'message':'Email alreay exits!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({'message':'User registerd'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Data is not valid'},status=status.HTTP_400_BAD_REQUEST)
        

        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenSerializer



class GetUser(APIView):
    permission_classes = [IsAdmin]

    def get(self):
        users = User.objects.all()
        if not users.exists():
            return Response({'message':'No user is present'},status=status.HTTP_400_BAD_REQUEST)
        
        serialisedUsers = UserSerializers(users,many=True)
        
        return Response({'message':'Users founded.','data':serialisedUsers.data},status=status.HTTP_200_OK)


class SoftDeleteaUser(APIView):
    permission_classes = [IsAdmin]

    def put(self,request):
        id = request.id
        userExit = User.objects.filter(id=id).first()
        if not userExit:
            return Response({'message':'Invalid id!'},status=status.HTTP_400_BAD_REQUEST)
        
        userExit.is_active = False
        return Response({'message':'Soft deleted a user.'},status=status.HTTP_200_OK)


    
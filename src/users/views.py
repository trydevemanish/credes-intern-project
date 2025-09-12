from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import UserSerializers,UserTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.permissions import IsAdmin,IsActiveUser
from rest_framework.permissions import AllowAny
from .models import CustomUser


# Create your views here.

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            checkUserExit = CustomUser.objects.filter(email=email).exists()
            if checkUserExit:
                print('Email already exits!')
                return Response({'message':'Email alreay exits!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                user=serializer.save()
                user.set_password(serializer.validated_data["password"])
                user.save()
                return Response({'message':'User registerd'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Data is not valid'},status=status.HTTP_400_BAD_REQUEST)
        

        
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    
    print('request received')
    serializer_class = UserTokenSerializer
    # print('seializer_class',serializer_class)



class GetUsers(APIView):
    permission_classes = [IsAdmin]

    def get(self,request):
        users = CustomUser.objects.filter(role='User').all()
        if not users.exists():
            return Response({'message':'No user is present'},status=status.HTTP_400_BAD_REQUEST)
        
        serialisedUsers = UserSerializers(users,many=True)
        
        return Response({'message':'Users founded.','data':serialisedUsers.data},status=status.HTTP_200_OK)


class SoftDeleteaUser(APIView):
    permission_classes = [IsAdmin]

    def put(self,request,id,*args, **kwargs):
        print(id)
        userExit = CustomUser.objects.filter(id=id).first()
        if not userExit:
            return Response({'message':'Invalid id!'},status=status.HTTP_400_BAD_REQUEST)
        
        userExit.is_active = False
        userExit.save()
        return Response({'message':f'Soft deleted a user with id: {id}.'},status=status.HTTP_200_OK)


    
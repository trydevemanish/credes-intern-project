from rest_framework import status
from django.http import JsonResponse
from .serializers import UserSerializers
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def RegisterUser(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            checkUserExit = User.objects.filter(email=serializer.data.email).first()
            if checkUserExit:
                print('Email already exits!')
                return JsonResponse({'message':'Email alreay exits!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return JsonResponse({'message':'User registerd'},status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message':'Data is not valid'},status=status.HTTP_400_BAD_REQUEST)
        
    return JsonResponse({'message':'Req method is not suitable.'},status=status.HTTP_400_BAD_REQUEST)


def LoginUser():
    ...


def GetUsers():
    ...
    
def SoftDeleteaUser():
    ...
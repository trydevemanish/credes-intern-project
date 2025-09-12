from rest_framework import status
from rest_framework.permissions import AllowAny # this allows to make req even if user is unauthorised.
from rest_framework.response import Response
from rest_framework.decorators import APIView

class Healthreq(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        return Response({'message':'Everything is fine, Server is healthy!'},status=status.HTTP_200_OK)
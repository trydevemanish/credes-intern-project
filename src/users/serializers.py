from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = '__all__'



class UserTokenSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        
        if not self.user.is_active:
            raise serializers.ValidationError('You cannot login(softly deleted)!')
        
        data['email'] = self.user.email
        data['role']  = self.user.role

        return data
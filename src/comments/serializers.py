from .models import Comment
from rest_framework import serializers


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = '__all__'

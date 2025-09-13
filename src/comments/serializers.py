from .models import Comment
from rest_framework import serializers


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = '__all__'
        read_only_fields = ['id','task','author','created_at']

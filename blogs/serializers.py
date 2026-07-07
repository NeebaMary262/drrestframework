from rest_framework import serializers
from .models import Blog, Comment
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
class BlogSerializer(serializers.ModelSerializer):
    comments =commentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
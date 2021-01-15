from django.contrib.auth.models import User
from .models import Post, Comment, Vote
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model User
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for model Post conne ted with serializer UserSerializer
    """
    author = UserSerializer
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['author', 'title', 'link', 'creation_date', 'amount_upvotes']


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for model Vote
    Connected to PostSerializer, UserSerializer
    """
    post = PostSerializer
    post = serializers.ReadOnlyField(source='post.title')
    user = UserSerializer
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Vote
        fields = '__all__'



class CommentsSerializer(serializers.ModelSerializer):
    """
    Serializer for model Comment
    Connected to PostSerializer, UserSerializer
    """
    post = PostSerializer
    post = serializers.ReadOnlyField(source='post.title')
    author = UserSerializer
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = '__all__'
        

class CommentsToPostSerializer(serializers.ModelSerializer):
    """
    Comment Serializer has only one Field
    Used for method POST
    """
    class Meta:
        model = Comment
        fields = ['comment']


        



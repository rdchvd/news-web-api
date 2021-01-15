from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from django.http import Http404

from .models import Post, Comment, Vote
from .serializers import PostSerializer, CommentsSerializer, UserSerializer, CommentsToPostSerializer, VoteSerializer

from django.contrib.auth.models import User




""""
CRUD API FOR POST DONE WITH GENERICS API
"""

class PostListGetApi(ListAPIView):
    """
    Class for otputting the list of news(posts)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateApi(CreateAPIView):
    """
    Class for creating a new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostGetDeleteUpdateApi(RetrieveUpdateDestroyAPIView):
    """
    Class for displaying post details, as well as for modifying and removing it
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'



""""
CRUD API FOR COMMENT DONE WITH GENERICS API
"""

class CommentCreateApi(CreateAPIView):
    """
    Class for creating a new comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsToPostSerializer
    
    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['postId'])
        serializer.save(author=self.request.user, post=post)


class CommentGetDeleteUpdateApi(RetrieveUpdateDestroyAPIView):
    """
    Class for displaying comment details, as well as for modifying and removing it
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = 'id'

class CommentListGetApi(ListAPIView):
    """
    Class for otputting the list of comments
    """
    serializer_class = CommentsSerializer
    def get_queryset(self):
        if 'postId' in self.kwargs.keys():
            queryset = Comment.objects.filter(post_id=self.kwargs['postId'])
        else:
            queryset = Comment.objects.all()
        return queryset
    
    
class VoteCreateApi(APIView):
    """
    Class for upvoting the post
    """

    def post(self, request, postId):
    
        post = Post.objects.get(id=postId)
        user = request.user
        vote = Vote.objects.filter(user=user, post=post).all()
        if not vote:
            vote = Vote(user=user, post=post)
            vote.save()
        return Response(status=200)






""""
CRUD API FOR COMMENT DONE WITH APIView

It is not used in the application 
because there`s enough functionality of generics api

Just another way to write an api
"""


class CommentView(APIView):

    def get_object(self, postId=None):
        """
        Method used for getting list of all comments
                or comments for the one new(post)
        """
        try:
            if postId:
                return Comment.objects.filter(post_id=postId)
            else:
                return Comment.objects.all()
        except Comment.DoesNotExist:
            return Http404


    def get(self, request, postId=None):
        """
        Method for ouputting comments
        """
        comments = self.get_object(postId)
        serializer = CommentsSerializer(comments, many = True)
        return Response(serializer.data)

    
    def post(self, request, postId):
        """
        Method for creating a new comment for the new(post)
        """
        if postId:
            data = request.data
            data['post'] = postId
            comment = CommentsSerializer(data=data)
            if comment.is_valid():
                comment.save()
            else:
                return Response(serializer.data)

            return self.get(self, request, postId)

        else:
            return Response(status=400)
    

    def delete(self, request, postId):
        """
        Method used for deleting a comment
        """
        comment = Comment.objects.get(id=postId)
        comment = CommentsSerializer(comment)
        try:
            comment.delete()
            return Response(status=200)

        except:
            return Response(status=400)


    def update(self, request, postId):
        """
        Method used for modifying a comment
        """
        comment = Comment.objects.get(id=postId)
        comment = CommentsSerializer(comment)
        try:
            comment.update()
            return Response(status=200)
        except:
            return Response(status=400)


    

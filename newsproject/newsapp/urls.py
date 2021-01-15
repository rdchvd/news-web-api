from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.PostListGetApi.as_view(), name='posts'),
    path('news/create/', views.PostCreateApi.as_view(), name='new_post'),
    path('news/<int:id>/', views.PostGetDeleteUpdateApi.as_view(), name='post_detail'),

    path('comments/', views.CommentListGetApi.as_view(), name='all_comments'),
    path('news/<int:postId>/comments/', views.CommentListGetApi.as_view(), name='comments_to_post'),
    path('news/<int:postId>/comments/create/', views.CommentCreateApi.as_view(), name='new_comment'),
    path('news/<int:postId>/comments/<int:id>/', views.CommentGetDeleteUpdateApi.as_view(), name='comment_detail'),
   
    path('news/<int:postId>/upvote/', views.VoteCreateApi.as_view(), name='upvote'),    
]

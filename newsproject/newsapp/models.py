from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class for table newsapp_post
    Used for news(posts)
    Connected to User, Vote
    Ordered by creation_date
    """

    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE, null=True
    )
    votes = models.ManyToManyField(
        "auth.User", through="Vote", related_name="votes_all"
    )

    @property
    def amount_upvotes(self):
        return self.votes.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["creation_date"]


class Vote(models.Model):
    """
    Class for table newsapp_vote
    Used to upvote news(posts)
    Connected to User, Post
    """

    post = models.ForeignKey(
        Post, related_name="votes_post", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "auth.User", related_name="votes_user", on_delete=models.CASCADE, null=True
    )


class Comment(models.Model):

    """
    Class for table newsapp_comment
    Used for comments
    Connected to User, Post
    Ordered by creation_date
    """

    author = models.ForeignKey(
        "auth.User", related_name="comments", on_delete=models.CASCADE, null=True
    )
    comment = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["creation_date"]

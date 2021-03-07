from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Blog post model
    title: Post title - VARCHAR in db
    slug: Used for SEO friendly blog posts urls creation,
        unique_for_date will make sure that 2 posts created at the same time
        don't have same urls
    author: Each post written by only 1 user, this user can write many posts
        deleting user will also mean deleting his posts
    body: Post content - TEXT in db
    publish: Post publication date with timezone support
    created: auto_now_add will create
        immutable date for when the post was created
    updated: auto_now will update this field to current date
        each time the model is saved
    status: Post status - restricted by STATUS_CHOICES
    """

    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0]
    )

    class Meta:
        """Order by lastly published so that new posts are up top"""

        ordering = ("-publish",)

    def __str__(self):
        """Title as string representation"""
        return self.title

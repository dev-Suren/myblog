from email.policy import default
from operator import mod
from wsgiref.simple_server import demo_app
from django.db import models
from django.forms import CharField
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from .helper import *

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.png', upload_to='user_profile')

    def __str__(self):
        return f'{self.user.username} Profile'


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    features_fild = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = ['created_at']


class Comment(models.Model):
    post = models.ForeignKey(
        BlogModel, related_name="comments", on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"

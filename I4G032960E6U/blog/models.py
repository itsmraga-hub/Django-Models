from django.db import models

# import User to use as foreign key
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """A model for blog"""
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Recipe(models.Model):
    title = models.CharField(max_length=600)
    subtitle = models.CharField(max_length=600)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipies')
    intro = models.CharField(max_length=600)
    steps = models.CharField(max_length=600)
    summary = models.CharField(max_length=600)
    likes = models.JSONField()
    comments = models.JSONField()

    def __string__(self):
        return self.title

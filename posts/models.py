from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    api_key = models.CharField(max_length=256, unique=True, blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
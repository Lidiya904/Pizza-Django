from datetime import *
from django.utils import timezone

from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    text = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True, help_text='о себе')
    date_of_birth = models.DateField(null=True, blank=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='tweet')
    twitext = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.date}'

    class Meta:
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    pos_id = models.IntegerField('ID поста', default=1, max_length=100)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='comment_author')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} {self.created}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    user_like = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='like_of_user')


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Publication(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    img = models.ImageField(default='default.jpg', upload_to='profile', null=True, blank=True)

    def __str__(self):
        return f'{self.uname.username}: {self.content}'


class PublicationW(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsw')
    img = models.ImageField(default=User, upload_to='profile', null=True, blank=True)

    def __str__(self):
        return f'{self.uname.username}: {self.content}'


class PublicationI(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsi')
    img = models.ImageField(default='default.jpg', upload_to='profile', null=True, blank=True)

    def __str__(self):
        return f'{self.uname.username}: {self.content}'

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile', blank=True)
    bio = models.TextField(default='')
    email_confirmed = models.BooleanField(default=False)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}'



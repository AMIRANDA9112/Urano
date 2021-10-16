from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.


class Publication(models.Model):
    text = models.TextField(default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    img = models.ImageField(upload_to='profile',
                            null=True,
                            blank=True)

    img2 = models.ImageField(upload_to='profile/%Y',
                             null=True,
                             blank=True)

    video = models.FileField(null=True,
                             blank=True,
                             upload_to='profile/%Y',
                             validators=[FileExtensionValidator(['mp4'])])

    pdf = models.FileField(null=True,
                           blank=True,
                           upload_to='profile/%Y',
                           validators=[FileExtensionValidator(['pdf'])])


class PublicationW(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsw')
    case_id = models.CharField(max_length=80, default='')
    datatime = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')
    img = models.ImageField(default=User, upload_to='profile', null=True, blank=True)


class PublicationI(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsi')
    img = models.ImageField(default='default.jpg', upload_to='profile', null=True, blank=True)

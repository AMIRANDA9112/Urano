from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.

class Publication(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')


class ImgPublication(models.Model):
    puname = models.ForeignKey(Publication,
                               on_delete=models.CASCADE,
                               related_name='img_publications',
                               null=True,
                               blank=True)
    img = models.ImageField(default='default.jpg',
                            upload_to='profile',
                            null=True,
                            blank=True)


class VideoPublication(models.Model):
    puname = models.ForeignKey(Publication,
                               on_delete=models.CASCADE,
                               related_name='video_publications',
                               null=True,
                               blank=True)
    video = models.FileField(null=True,
                             blank=True,
                             validators=[FileExtensionValidator(['mp4'])])


class PdfPublication(models.Model):
    puname = models.ForeignKey(Publication,
                               on_delete=models.CASCADE,
                               related_name='pdf_publications',
                               null=True, blank=True)
    pdf = models.FileField(null=True,
                           blank=True,
                           validators=[FileExtensionValidator(['pdf'])])


class PublicationW(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsw')
    img = models.ImageField(default=User, upload_to='profile', null=True, blank=True)


class PublicationI(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsi')
    img = models.ImageField(default='default.jpg', upload_to='profile', null=True, blank=True)

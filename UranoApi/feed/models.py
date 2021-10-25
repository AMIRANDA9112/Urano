from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from taggit.managers import TaggableManager



# Create your models here.


class Publication(models.Model):
    text = models.TextField(default='', verbose_name="Escriba Aqui", help_text="Espacio de Libre Expresión")
    tag_text = models.TextField(blank=True)
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    img = models.ImageField(upload_to='profile',
                            null=True,
                            blank=True,
                            verbose_name="Subir Imagen",
                            help_text=".PNG, .JPG, .JPEG"
                            )

    empty_img = models.BooleanField(default=False)

    img2 = models.ImageField(upload_to='profile/%Y',
                             null=True,
                             blank=True,
                             verbose_name="Subir Imagen",
                             help_text=".PNG, .JPG, .JPEG"
                             )

    empty_img2 = models.BooleanField(default=False)

    video = models.FileField(null=True,
                             blank=True,
                             upload_to='profile/%Y',
                             validators=[FileExtensionValidator(['mp4'])],
                             verbose_name="Subir Video",
                             help_text="Formato MP4"
                             )

    empty_video = models.BooleanField(default=False)

    pdf = models.FileField(null=True,
                           blank=True,
                           upload_to='profile/%Y',
                           validators=[FileExtensionValidator(['pdf'])]
                           , verbose_name="Subir Documento PDF")


    empty_pdf = models.BooleanField(default=False)

    slug = models.SlugField(unique=True, max_length=100, null=True,
                            blank=True)



    tags = TaggableManager()

    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


class PublicationW(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsw')
    case_id = models.CharField(max_length=80, default='', verbose_name="Titulo de la Alerta")
    datatime = models.DateTimeField(default=timezone.now)
    description = models.TextField(verbose_name="Describa la Alerta")
    tag_text = models.TextField(blank=True)
    involved = TaggableManager(verbose_name="Involucrados",)
    addresss = models.TextField( null=True,
                               blank=True)
    lat = models.FloatField(default=0, null=True,
                            blank=True)
    lon = models.FloatField(default=0, null=True,
                            blank=True)

    slug = models.SlugField(unique=True, max_length=100, null=True,
                            blank=True)
    img = models.ImageField(upload_to='profile', verbose_name="Subir Imagen",
                            help_text=".PNG, .JPG, .JPEG",
                            null=True,
                            blank=True)

    empty_img = models.BooleanField(default=False)

    img2 = models.ImageField(upload_to='profile/%Y',  verbose_name="Subir Imagen",
                            help_text=".PNG, .JPG, .JPEG",
                             null=True,
                             blank=True)

    empty_img2 = models.BooleanField(default=False)

    video = models.FileField(null=True,
                             blank=True,
                             upload_to='profile/%Y',
                             validators=[FileExtensionValidator(['mp4'])],
                             verbose_name="Subir Video",
                             help_text="Formato MP4")

    empty_video = models.BooleanField(default=False)

    pdf = models.FileField(null=True,
                           blank=True,
                           upload_to='profile/%Y',
                           validators=[FileExtensionValidator(['pdf'])],
                           verbose_name="Subir Documento PDF")

    empty_pdf = models.BooleanField(default=False)

    likes = models.ManyToManyField(User, blank=True, related_name='likesw')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikesw')


class PublicationI(models.Model):
    text = models.TextField(max_length=280, default='')
    datatime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicationsi')
    img = models.ImageField(default='default.jpg', upload_to='profile', null=True, blank=True)

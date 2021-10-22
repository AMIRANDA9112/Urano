# Generated by Django 3.2.3 on 2021-10-21 08:41

import django.core.validators
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='img',
            field=models.ImageField(blank=True, help_text='La imagen puede ser .PNG, .JPG, .JPEG', null=True, upload_to='profile', verbose_name='Subir Imagen'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='img2',
            field=models.ImageField(blank=True, help_text='La imagen puede ser .PNG, .JPG, .JPEG', null=True, upload_to='profile/%Y', verbose_name='Subir Imagen'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Subir Documento PDF'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(default='', help_text='Sientase libre de Expresarse', verbose_name='Escriba Aqui'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='video',
            field=models.FileField(blank=True, help_text='Video de Formato mp4 con menos de 20mb de Tamaño', null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['mp4'])], verbose_name='Subir Video'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='address',
            field=models.TextField(blank=True, default='Colombia', help_text="Pais, Departamento, Municipio, Vereda o Direccion exacta 'carrera #, calle #'", null=True, verbose_name='Escriba su Direccion o Ubicación'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='case_id',
            field=models.CharField(default='', max_length=80, verbose_name='Titulo de la Alerta'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='description',
            field=models.TextField(default='', verbose_name='Describa la Alerta'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='img',
            field=models.ImageField(blank=True, help_text='La imagen puede ser .PNG, .JPG, .JPEG', null=True, upload_to='profile', verbose_name='Subir Imagen'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='img2',
            field=models.ImageField(blank=True, help_text='La imagen puede ser .PNG, .JPG, .JPEG', null=True, upload_to='profile/%Y', verbose_name='Subir Imagen'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='involved',
            field=taggit.managers.TaggableManager(help_text='Funciona como Hastags o palabras Clave separadas por comas, menciones a Autoridades Competentes, Afectados o Zonas', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Involucrados'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Subir Documento PDF'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='video',
            field=models.FileField(blank=True, help_text='Video de Formato mp4 con menos de 20mb de Tamaño', null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['mp4'])], verbose_name='Subir Video'),
        ),
    ]

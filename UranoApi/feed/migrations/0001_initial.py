# Generated by Django 3.2.8 on 2021-10-21 02:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(default='', max_length=80)),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='')),
                ('address', models.TextField(blank=True, default='Colombia', null=True)),
                ('lat', models.FloatField(blank=True, default=0, null=True)),
                ('lon', models.FloatField(blank=True, default=0, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='profile/%Y')),
                ('video', models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['mp4'])])),
                ('pdf', models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikesw', to=settings.AUTH_USER_MODEL)),
                ('involved', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('likes', models.ManyToManyField(blank=True, related_name='likesw', to=settings.AUTH_USER_MODEL)),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicationsw', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=280)),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicationsi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='profile/%Y')),
                ('video', models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['mp4'])])),
                ('pdf', models.FileField(blank=True, null=True, upload_to='profile/%Y', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-01 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('feed', '0029_auto_20211101_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='publicationw',
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='CommentsW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('tag_text', models.TextField(blank=True)),
                ('datatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikescw', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likescw', to=settings.AUTH_USER_MODEL)),
                ('publicationw', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feed.publicationw')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsw', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

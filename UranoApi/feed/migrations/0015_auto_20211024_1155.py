# Generated by Django 3.2.8 on 2021-10-24 11:55

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('feed', '0014_remove_publicationw_locationmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationw',
            name='addresss',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='description',
            field=models.TextField(verbose_name='Describa la Alerta'),
        ),
        migrations.AlterField(
            model_name='publicationw',
            name='involved',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Involucrados'),
        ),
    ]

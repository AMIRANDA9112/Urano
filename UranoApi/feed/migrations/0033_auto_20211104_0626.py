# Generated by Django 3.2.8 on 2021-11-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0032_alter_publicationw_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationw',
            name='tag_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='publicationw',
            name='tag_category',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_auto_20211024_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='empty_img',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='empty_img2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='empty_pdf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='empty_video',
            field=models.BooleanField(default=False),
        ),
    ]

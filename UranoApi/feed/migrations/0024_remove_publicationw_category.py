# Generated by Django 3.2.8 on 2021-10-30 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0023_alter_publicationw_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationw',
            name='category',
        ),
    ]
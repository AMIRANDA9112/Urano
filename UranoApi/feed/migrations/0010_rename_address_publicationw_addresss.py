# Generated by Django 3.2.8 on 2021-10-23 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_alter_publicationw_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicationw',
            old_name='address',
            new_name='addresss',
        ),
    ]

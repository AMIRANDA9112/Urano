# Generated by Django 3.2.8 on 2021-10-31 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0027_comments_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='parent',
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(default='', help_text='Comentario de Libre Expresión'),
        ),
    ]

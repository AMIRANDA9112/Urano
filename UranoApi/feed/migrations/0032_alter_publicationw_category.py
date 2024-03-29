# Generated by Django 3.2.8 on 2021-11-03 01:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0031_auto_20211103_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationw',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Desaparicion', 'Desaparición'), ('DesplazamientoForzado', 'Desplazamiento Forzado'), ('PresenciaGruposArmados', 'Presencia Grupos Armados'), ('AbusoPolicial', 'Abuso Policial'), ('Extorsion', 'Extorsión'), ('Estafa', 'Estafa'), ('Deforestacion', 'Deforestación'), ('MaltratoIntrafamiliar', 'Maltrato Intrafamiliar'), ('ViolenciaDeGenero', 'Violencia de Genero'), ('ViolenciaSexual', 'Violencia Sexual'), ('Discriminacion', 'Discriminación'), ('ExplotacionLaboral', 'Explotación Laboral'), ('Corrupcion', 'Corrupción'), ('MaltratoAnimal', 'Maltrato Animal'), ('Deforestacion', 'Deforestación'), ('ContaminacionAmbiental', 'Contaminación Ambiental')], max_length=255, null=True),
        ),
    ]

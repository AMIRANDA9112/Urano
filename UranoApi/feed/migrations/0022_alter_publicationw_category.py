# Generated by Django 3.2.8 on 2021-10-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0021_alter_publicationw_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationw',
            name='category',
            field=models.TextField(blank=True, choices=[('ViolenciaPolicial', 'Violencia Policial'), ('ViolenciadeGenero', 'Violencia de Genero'), ('AcosoSexual', 'Acoso Sexual'), ('ExploacionSexual', 'Exploación Sexual'), ('MaltratoIntrafamiliar', 'Maltrato Intrafamiliar'), ('ExploacionLaboral', 'Exploación Laboral'), ('CorrupcionPublica', 'Corrupción Publica'), ('CorrupcionPrivada', 'Corrupción Privada'), ('MaltratoAnimal', 'Maltrato Animal'), ('Deforestacion', 'Deforestación'), ('MineriaIlegal', 'Minería Ilegal'), ('ContaminacionAmbiental', 'Contaminación Ambiental'), ('Desaparición', 'Desaparición')]),
        ),
    ]

# Generated by Django 2.2.4 on 2020-04-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0029_permisos_delete_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='prioridad',
            field=models.SmallIntegerField(choices=[('1', 'Alta'), ('2', 'Media'), ('3', 'Baja')], default=2),
        ),
    ]
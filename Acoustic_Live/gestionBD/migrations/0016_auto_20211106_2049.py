# Generated by Django 3.2.8 on 2021-11-07 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0015_auto_20211106_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellidoM_estudiante',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellidoP_estudiante',
            field=models.CharField(max_length=50),
        ),
    ]

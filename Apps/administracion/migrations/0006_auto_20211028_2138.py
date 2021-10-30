# Generated by Django 3.2.6 on 2021-10-29 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_periodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccion',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='seccion',
            name='seccion',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='M', max_length=20),
        ),
    ]

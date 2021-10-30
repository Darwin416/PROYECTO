# Generated by Django 3.2.6 on 2021-10-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('seccion', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('DESACTIVAR', 'DESACTIVAR')], default='M', max_length=20)),
                ('año', models.CharField(choices=[('2021', '2021'), ('2022', '2022')], default='M', max_length=20)),
            ],
        ),
    ]
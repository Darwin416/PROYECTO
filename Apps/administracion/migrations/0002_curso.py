# Generated by Django 3.2.6 on 2021-10-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('DESACTIVAR', 'DESACTIVAR')], default='M', max_length=20)),
            ],
        ),
    ]

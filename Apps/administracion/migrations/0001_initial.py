# Generated by Django 3.2.6 on 2021-10-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2023-02-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienestarwebApp', '0002_alter_paginas_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='contenido',
            field=models.TextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]

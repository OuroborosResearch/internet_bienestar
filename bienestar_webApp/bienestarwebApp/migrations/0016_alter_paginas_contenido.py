# Generated by Django 4.0.2 on 2023-02-28 19:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bienestarwebApp', '0015_alter_paginas_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]

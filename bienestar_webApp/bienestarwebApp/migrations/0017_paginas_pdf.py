# Generated by Django 4.0.2 on 2023-07-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienestarwebApp', '0016_alter_paginas_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginas',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pags/bienestarwebApp/pdfs'),
        ),
    ]

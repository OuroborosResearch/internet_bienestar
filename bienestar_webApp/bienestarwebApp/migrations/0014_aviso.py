# Generated by Django 4.0.2 on 2023-02-25 18:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienestarwebApp', '0013_entradas_imagen_alter_entradas_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Título')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Aviso de Privacidad',
                'verbose_name_plural': 'Aviso de Privacidad',
            },
        ),
    ]

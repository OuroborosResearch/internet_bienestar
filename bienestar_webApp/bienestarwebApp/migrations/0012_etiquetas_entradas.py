# Generated by Django 4.0.2 on 2023-02-13 02:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bienestarwebApp', '0011_delete_etiquetas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiquetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Etiquetas Blog',
                'verbose_name_plural': 'Etiquetas Blog',
            },
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('etiquetas', models.ManyToManyField(to='bienestarwebApp.Etiquetas')),
            ],
            options={
                'verbose_name': 'Entradas Blog',
                'verbose_name_plural': 'Entradas Blog',
            },
        ),
    ]
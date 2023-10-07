# Generated by Django 4.0.2 on 2023-02-13 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bienestarwebApp', '0012_etiquetas_entradas'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Imagen de portada'),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='autor',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

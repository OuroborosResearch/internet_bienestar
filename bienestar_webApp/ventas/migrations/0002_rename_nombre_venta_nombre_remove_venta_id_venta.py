# Generated by Django 4.0.2 on 2023-12-20 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_venta',
        ),
    ]

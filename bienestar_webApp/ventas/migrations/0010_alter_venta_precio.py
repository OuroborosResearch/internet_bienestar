# Generated by Django 4.0.2 on 2023-12-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_alter_venta_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio',
            field=models.IntegerField(choices=[(100, 'Obten tu Chip'), (50, 'Paquete 50'), (65, 'Paquete 65'), (100, 'Paquete 100'), (125, 'Paquete 125'), (200, 'Paquete 200')]),
        ),
    ]
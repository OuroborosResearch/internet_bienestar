# Generated by Django 4.0.2 on 2023-12-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_alter_venta_cantidad_alter_venta_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio',
            field=models.IntegerField(choices=[(50, 'Plan 50'), (65, 'Plan 65'), (100, 'Plan 100'), (125, 'Plan 125'), (200, 'Plan 200')]),
        ),
    ]
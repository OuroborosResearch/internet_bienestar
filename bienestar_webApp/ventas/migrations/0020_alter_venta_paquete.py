# Generated by Django 4.0.2 on 2024-07-16 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0019_alter_venta_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='paquete',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

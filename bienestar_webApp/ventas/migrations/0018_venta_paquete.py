# Generated by Django 4.0.2 on 2024-07-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0017_remove_venta_paquete_alter_venta_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='paquete',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]

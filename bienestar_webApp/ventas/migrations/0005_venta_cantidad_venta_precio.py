# Generated by Django 4.0.2 on 2023-12-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_alter_venta_no_int'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='venta',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]

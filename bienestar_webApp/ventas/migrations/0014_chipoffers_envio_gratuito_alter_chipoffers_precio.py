# Generated by Django 4.0.2 on 2024-07-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0013_chipoffers_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipoffers',
            name='envio_gratuito',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chipoffers',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
# Generated by Django 4.0.2 on 2023-02-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienestarwebApp', '0014_aviso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='pags/bienestarwebApp/terminos'),
        ),
    ]

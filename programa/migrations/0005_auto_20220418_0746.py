# Generated by Django 3.2.9 on 2022-04-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0004_implementasaun_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='implementasaun',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='implementasaun',
            name='montanteOsanAlokasaun',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Orsamentu Alokasaun'),
        ),
    ]

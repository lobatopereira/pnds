# Generated by Django 3.2.9 on 2022-04-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsionariu', '0003_rename_aldeia_funsionariu_aldeia'),
    ]

    operations = [
        migrations.AddField(
            model_name='funsionariu',
            name='tipu_f',
            field=models.CharField(blank=True, choices=[('Fun', 'Funsionariu'), ('EIP', 'Ekipa Implementasaun Programa')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funsionariu',
            name='seksu',
            field=models.CharField(blank=True, choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=10, null=True),
        ),
    ]
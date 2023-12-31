# Generated by Django 3.1.1 on 2022-01-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_auto_20220105_2234'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Sistema',
        ),
        migrations.RemoveField(
            model_name='monitoring',
            name='sistema_implementasaun',
        ),
        migrations.RemoveField(
            model_name='programa',
            name='tags',
        ),
        migrations.AddField(
            model_name='monitoring',
            name='sistema',
            field=models.ManyToManyField(to='monitoring.Sistema'),
        ),
        migrations.AlterField(
            model_name='monitoring',
            name='komentariu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

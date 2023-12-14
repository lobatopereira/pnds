# Generated by Django 3.1.1 on 2022-01-05 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_auto_20220105_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoring',
            name='funs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.funsionariu'),
        ),
        migrations.AddField(
            model_name='monitoring',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.programa'),
        ),
    ]
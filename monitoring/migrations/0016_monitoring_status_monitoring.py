# Generated by Django 3.1.1 on 2022-01-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0015_auto_20220106_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoring',
            name='status_monitoring',
            field=models.CharField(choices=[('Monitoring ona', 'Monitoring ona'), ('Seidauk Monitoring', 'Seidauk Monitoring')], max_length=100, null=True),
        ),
    ]

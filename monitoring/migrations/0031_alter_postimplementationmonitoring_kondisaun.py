# Generated by Django 3.2.9 on 2022-05-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0030_auto_20220510_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimplementationmonitoring',
            name='kondisaun',
            field=models.CharField(blank=True, choices=[('Diak', 'Diak'), ('Normal', 'Normal'), ('Aat', 'Aat')], max_length=30, null=True),
        ),
    ]

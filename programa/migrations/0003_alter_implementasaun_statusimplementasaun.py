# Generated by Django 3.2.9 on 2022-03-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0002_alter_programa_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementasaun',
            name='statusImplementasaun',
            field=models.CharField(blank=True, choices=[('Uza Ona', 'Uza Ona'), ('Seidauk Uza', 'Seidauk Uza')], max_length=30, null=True),
        ),
    ]

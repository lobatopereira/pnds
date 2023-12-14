# Generated by Django 3.2.9 on 2022-05-08 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0009_auto_20220508_1416'),
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='implementasaun',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.survey'),
        ),
        migrations.AddField(
            model_name='implementasaun',
            name='totalTekniku',
            field=models.IntegerField(null=True, verbose_name='Total Tekniku'),
        ),
        migrations.AlterField(
            model_name='implementasaun',
            name='statusImplementasaun',
            field=models.CharField(blank=True, choices=[('Not Start', 'Not Start'), ('On Going', 'On Going'), ('Pending', 'Pending'), ('Abandone', 'Abandone'), ('Complate', 'Complate')], default='Not Start', max_length=30, null=True),
        ),
    ]

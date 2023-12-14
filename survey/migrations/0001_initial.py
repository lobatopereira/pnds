# Generated by Django 3.2.9 on 2022-05-08 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom', '0001_initial'),
        ('programa', '0009_auto_20220508_1416'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aldeia', models.CharField(blank=True, max_length=222, null=True, verbose_name="Survey iha Aldeia ka bairu ne'ebe?")),
                ('surveyDate', models.DateField(null=True, verbose_name='Data Survey')),
                ('totalUmakain', models.IntegerField(null=True, verbose_name='Total Umakain')),
                ('image', models.ImageField(blank=True, null=True, upload_to='SurveyImage', verbose_name='Upload Imajen Survey')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Informasaun Adisional')),
                ('is_locked', models.BooleanField(blank=True, default=False, null=True)),
                ('is_sent', models.BooleanField(blank=True, default=False, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('is_rejected', models.BooleanField(blank=True, default=False, null=True)),
                ('rejected_info', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('administrativepost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.administrativepost', verbose_name="Survey iha Postu ne'ebe?")),
                ('municipality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.municipality', verbose_name="Survey iha Munisipiu ne'ebe?")),
                ('programa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programa.programa')),
                ('user_created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('village', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.village', verbose_name="Survey iha Suku ne'ebe?")),
            ],
        ),
    ]

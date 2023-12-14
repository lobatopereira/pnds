# Generated by Django 3.2.9 on 2022-02-27 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funsionariu', '0001_initial'),
        ('monitoring', '0023_remove_monitoring_status_monitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementationMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pursentu_programa', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Pursetu Implementasaun')),
                ('orsamentu_gastu', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Orsamentu Gastus')),
                ('partisipasaun_feto', models.CharField(max_length=200, null=True)),
                ('ekipamentu_lakompletu', models.CharField(max_length=200, null=True)),
                ('komentariu', models.TextField(blank=True, null=True)),
                ('monitoring_date', models.DateField()),
                ('faze', models.CharField(choices=[('Dahuluk I', 'Dahuluk I'), ('Daruak II', 'Daruak II'), ('Datoluk III', 'Datoluk III'), ('Dahaat IV', 'Dahaat IV'), ('Dalima V', 'Dalima V'), ('Daneen VI', 'Daneen VI'), ('Dahitu VII', 'Dahitu VII')], max_length=200, null=True)),
                ('siklu', models.CharField(max_length=200, null=True)),
                ('statusImplementasaun', models.CharField(choices=[('Foin hahuu', 'Foin hahuu'), ('Sei iha klaran ', 'Sei iha klaran '), ('Hotu ona', 'Hotu ona')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostImplementationMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitoring_date', models.DateField()),
                ('kondisaun', models.CharField(blank=True, choices=[('Diak', 'Diak'), ('Aat', 'Aat')], max_length=30, null=True)),
                ('komentariu', models.TextField(blank=True, null=True)),
                ('rekomendasaun', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('funsionariu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='funsionariu.funsionariu')),
            ],
        ),
        migrations.RemoveField(
            model_name='monitoring',
            name='funs',
        ),
        migrations.RemoveField(
            model_name='monitoring',
            name='program',
        ),
        migrations.RemoveField(
            model_name='monitoring',
            name='sistem',
        ),
        migrations.RemoveField(
            model_name='monitoring',
            name='suku',
        ),
        migrations.DeleteModel(
            name='Funsionariu',
        ),
        migrations.DeleteModel(
            name='Monitoring',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
        migrations.DeleteModel(
            name='Sistema',
        ),
        migrations.DeleteModel(
            name='Suku',
        ),
    ]
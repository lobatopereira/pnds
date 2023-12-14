# Generated by Django 3.2.9 on 2022-05-08 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
        ('funsionariu', '0007_alter_funsionariu_aldeia'),
    ]

    operations = [
        migrations.AddField(
            model_name='funsionariu',
            name='areaadministrativepost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaAdministrativePost', to='custom.administrativepost'),
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='areamunicipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaMunicipality', to='custom.municipality'),
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='areavillage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaVillage', to='custom.village'),
        ),
        migrations.AlterField(
            model_name='funsionariu',
            name='administrativepost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AdministrativePost', to='custom.administrativepost'),
        ),
        migrations.AlterField(
            model_name='funsionariu',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Municipality', to='custom.municipality'),
        ),
        migrations.AlterField(
            model_name='funsionariu',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Village', to='custom.village'),
        ),
    ]

# Generated by Django 3.1.1 on 2022-01-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0010_auto_20220105_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoring',
            name='pozisaun',
            field=models.CharField(choices=[('Ekipa Jestaun Suku (EIP)', 'Ekipa Jestaun Suku (EIP)'), ('Fasilitador Tekniku Postu Administrativu Atauro', 'Fasilitador Tekniku Postu Administrativu Atauro'), ('Fasilitador Tekniku Postu Administrativu Cristo rei', 'Fasilitador Tekniku Postu Administrativu Cristo rei'), ('Fasilitador Tekniku Postu Administrativu Dom Aleixo', 'Fasilitador Tekniku Postu Administrativu Dom Aleixo'), ('Fasilitador Tekniku Postu Administrativu Metinaru', 'Fasilitador Tekniku Postu Administrativu Metinaru'), ('Fasilitador Tekniku Postu Administrativu Nain Feto', 'Fasilitador Tekniku Postu Administrativu Nain Feto'), ('Fasilitador Tekniku Postu Administrativu Vera-Cruz', 'Fasilitador Tekniku Postu Administrativu Vera-Cruz'), ('Direktor', 'Direktor')], max_length=200, null=True),
        ),
    ]
# Generated by Django 5.0.4 on 2024-06-19 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('piece', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donnees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('valeur', models.FloatField()),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.capteurs')),
            ],
        ),
    ]

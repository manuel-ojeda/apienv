# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('races', '0001_initial'),
        ('factions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female')], max_length=10)),
                ('faction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, serialize=False, to='factions.Faction')),
                ('race', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='races.Race')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]

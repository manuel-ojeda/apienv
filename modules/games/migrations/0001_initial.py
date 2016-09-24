# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('map', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maps.Map')),
                ('game_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, serialize=False, to='games.GameType')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateField()),
                ('finished_at', models.DateField()),
                ('winner_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
    ]

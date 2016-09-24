# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female')], max_length=10)),
            ],
        ),
    ]

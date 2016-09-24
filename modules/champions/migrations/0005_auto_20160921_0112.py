# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-21 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0004_auto_20160921_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='faction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='champions', to='factions.Faction'),
        ),
    ]
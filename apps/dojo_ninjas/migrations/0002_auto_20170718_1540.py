# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='dojo_id',
        ),
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.Dojo'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniclerval', '0001_initial'),
        ('cdbmeta', '0006_cdbrecord_nheader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribution',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='attribution',
            name='name',
        ),
        migrations.AddField(
            model_name='attribution',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='miniclerval.Person'),
            preserve_default=False,
        ),
    ]

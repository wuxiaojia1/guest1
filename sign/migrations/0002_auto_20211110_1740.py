# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2021-11-10 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='starttime',
            new_name='start_time',
        ),
    ]

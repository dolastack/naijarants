# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rants', '0010_auto_20171227_0115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rant',
            options={'ordering': ['-time_created']},
        ),
    ]

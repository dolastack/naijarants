# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 03:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rants', '0007_rant_catigory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rant',
            old_name='catigory',
            new_name='category',
        ),
    ]
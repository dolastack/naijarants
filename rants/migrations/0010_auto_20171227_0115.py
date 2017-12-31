# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 01:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rants', '0009_auto_20171227_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rant',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
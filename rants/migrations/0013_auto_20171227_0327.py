# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rants', '0012_auto_20171227_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='rant',
            options={'ordering': ['-time_created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='rant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rants.Rant'),
        ),
    ]

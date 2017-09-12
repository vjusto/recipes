# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('preparation_time', models.IntegerField()),
                ('ingredients_list', models.TextField(default='[]')),
                ('instructions_list', models.TextField(default='[]')),
            ],
        ),
    ]

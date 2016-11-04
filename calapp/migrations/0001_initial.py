# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('allday', models.BooleanField()),
                ('description', models.TextField()),
                ('synced', models.BooleanField(default=False)),
            ],
        ),
    ]
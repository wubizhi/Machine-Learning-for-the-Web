# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addressesapp', '0002_remove_person_mobilephone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160912_2107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hello',
            new_name='Member',
        ),
    ]

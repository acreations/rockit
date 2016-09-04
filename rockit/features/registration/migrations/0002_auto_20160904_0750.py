# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='identifier',
            field=models.UUIDField(help_text='Unique identifier (uuid4)', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='hello',
            name='message',
            field=models.TextField(help_text='Any hello message?', max_length=1000),
        ),
        migrations.AlterField(
            model_name='hello',
            name='name',
            field=models.TextField(help_text='Please specify a name', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-07 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='name',
            new_name='location',
        ),
    ]
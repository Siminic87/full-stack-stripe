# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-07 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_voter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='upvotes',
            new_name='post',
        ),
    ]
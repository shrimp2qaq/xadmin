# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-03-27 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavorite',
            old_name='course',
            new_name='fav_id',
        ),
    ]

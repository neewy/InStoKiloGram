# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='pic_folder/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0003_auto_20180119_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weblog.Category', verbose_name='Parent category'),
        ),
    ]
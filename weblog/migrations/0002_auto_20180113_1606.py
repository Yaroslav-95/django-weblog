# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('parent_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='weblog.Category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('language', models.CharField(max_length=5, verbose_name='Language (ISO)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category name translation',
                'verbose_name_plural': 'Category name translations',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='original_language',
            field=models.CharField(blank=True, max_length=5, verbose_name='Original language (ISO)'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weblog.Category', verbose_name='Category'),
        ),
    ]

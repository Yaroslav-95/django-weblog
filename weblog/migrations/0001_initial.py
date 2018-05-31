# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('preview_image', models.ImageField(blank=True, upload_to='weblog/preview_images/%Y/%m/%d/', verbose_name='Preview image')),
                ('preview_text', models.CharField(blank=True, max_length=250, verbose_name='Preview Text')),
                ('original_language', models.CharField(max_length=5, verbose_name='Original language (ISO)')),
                ('publish_date', models.DateTimeField(verbose_name='Publish date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.BlogPost', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=5, verbose_name='Language (ISO)')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('preview_image', models.ImageField(blank=True, upload_to='weblog/preview_images/%Y/%m/%d/', verbose_name='Preview image')),
                ('preview_text', models.CharField(blank=True, max_length=250, verbose_name='Preview Text')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.BlogPost', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]

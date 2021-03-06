# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='admin',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='moderator',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='professional',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='verified_user',
            field=models.NullBooleanField(default=False),
        ),
    ]

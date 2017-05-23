# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_auto_20170521_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='poses',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poses',
            name='chakra_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poses',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poses',
            name='difficulty_level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poses',
            name='pose_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_video',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='users',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_picture_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
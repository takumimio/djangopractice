# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='softjob',
            name='author',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='softjob',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='softjob',
            name='page_index',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='softjob',
            name='time',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='softjob',
            name='title',
            field=models.CharField(null=True, max_length=100),
        ),
    ]

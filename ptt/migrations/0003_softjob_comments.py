# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptt', '0002_auto_20161111_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='softjob',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]

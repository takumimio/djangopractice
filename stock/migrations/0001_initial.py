# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('symbol', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('open', models.DecimalField(max_digits=18, decimal_places=4)),
                ('high', models.DecimalField(max_digits=18, decimal_places=4)),
                ('low', models.DecimalField(max_digits=18, decimal_places=4)),
                ('close', models.DecimalField(max_digits=18, decimal_places=4)),
                ('volume', models.BigIntegerField()),
            ],
        ),
    ]

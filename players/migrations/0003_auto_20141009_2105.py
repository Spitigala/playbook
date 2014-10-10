# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20141009_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 9), auto_now=True),
            preserve_default=False,
        ),
    ]

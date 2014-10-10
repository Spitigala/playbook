# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20141009_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 9), auto_now_add=True),
            preserve_default=False,
        ),
    ]

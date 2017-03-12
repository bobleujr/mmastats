# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0005_auto_20160509_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='code',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]

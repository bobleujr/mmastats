# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0008_auto_20170204_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='ufc',
            field=models.BooleanField(default=False),
        ),
    ]

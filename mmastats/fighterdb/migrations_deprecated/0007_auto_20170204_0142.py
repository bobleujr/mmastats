# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0006_fighter_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='code',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]

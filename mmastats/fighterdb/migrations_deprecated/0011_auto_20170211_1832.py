# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0010_eventmetric_fightermetric_fightmetric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fightmetric',
            name='fighter1',
            field=models.CharField(max_length=30, null=True, db_column=b'fighter1_id', blank=True),
        ),
        migrations.AlterField(
            model_name='fightmetric',
            name='fighter2',
            field=models.CharField(max_length=30, null=True, db_column=b'fighter2_id', blank=True),
        ),
    ]

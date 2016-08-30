# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0003_auto_20160318_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='height',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='weight',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=4, blank=True),
            preserve_default=True,
        ),
    ]

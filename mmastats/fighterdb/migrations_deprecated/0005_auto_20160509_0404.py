# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0004_auto_20160509_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='height',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='weight',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
            preserve_default=True,
        ),
    ]

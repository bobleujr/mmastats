# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0007_auto_20170204_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]

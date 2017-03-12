# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0011_auto_20170211_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='fightermetric',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='code',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='height',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='nick_name',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='reach',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='sapm',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='slpm',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='stracc',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='strdef',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='subavg',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='tdacc',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='tdavg',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='tddef',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fightermetric',
            name='weight',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='fightermetric',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]

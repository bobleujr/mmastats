# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0002_auto_20160315_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='event_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='fight_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='fight_result_type',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='fighter1',
            field=models.IntegerField(null=True, db_column=b'fighter1_id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='fighter2',
            field=models.IntegerField(null=True, db_column=b'fighter2_id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='fighter_winner',
            field=models.IntegerField(null=True, db_column=b'fighter_winner_id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='referee',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='round',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fight',
            name='time',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='country',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='l_decisions',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='l_kos_tkos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='l_submissions',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='locality',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='loss_counter',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='nick_name',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='team',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='w_decisions',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='w_kos_tkos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='w_submissions',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='weight_class',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fighter',
            name='win_counter',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

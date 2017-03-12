# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighterdb', '0009_fighter_ufc'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMetric',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hasher', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FighterMetric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='FightMetric',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fighter1', models.IntegerField(null=True, db_column=b'fighter1_id', blank=True)),
                ('fighter2', models.IntegerField(null=True, db_column=b'fighter2_id', blank=True)),
                ('str1', models.IntegerField(null=True, blank=True)),
                ('str2', models.IntegerField(null=True, blank=True)),
                ('td1', models.IntegerField(null=True, blank=True)),
                ('td2', models.IntegerField(null=True, blank=True)),
                ('sub1', models.IntegerField(null=True, blank=True)),
                ('sub2', models.IntegerField(null=True, blank=True)),
                ('pass1', models.IntegerField(null=True, blank=True)),
                ('pass2', models.IntegerField(null=True, blank=True)),
                ('round', models.IntegerField(null=True, blank=True)),
                ('time', models.CharField(max_length=10, null=True, blank=True)),
                ('event', models.ForeignKey(to='fighterdb.EventMetric')),
            ],
        ),
    ]

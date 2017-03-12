# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Fight',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fighter1', models.IntegerField(null=True, db_column=b'fighter1_id', blank=True)),
                ('fighter2', models.IntegerField(null=True, db_column=b'fighter2_id', blank=True)),
                ('fighter_winner', models.IntegerField(null=True, db_column=b'fighter_winner_id', blank=True)),
                ('fight_date', models.DateField(null=True, blank=True)),
                ('event_id', models.IntegerField(null=True, blank=True)),
                ('fight_result_type', models.CharField(max_length=50, null=True, blank=True)),
                ('referee', models.CharField(max_length=150, null=True, blank=True)),
                ('round', models.IntegerField(null=True, blank=True)),
                ('time', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('nick_name', models.CharField(max_length=300, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('locality', models.CharField(max_length=300, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('height', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('weight_class', models.CharField(max_length=80, null=True, blank=True)),
                ('team', models.CharField(max_length=150, null=True, blank=True)),
                ('win_counter', models.IntegerField(null=True, blank=True)),
                ('w_kos_tkos', models.IntegerField(null=True, blank=True)),
                ('w_submissions', models.IntegerField(null=True, blank=True)),
                ('w_decisions', models.IntegerField(null=True, blank=True)),
                ('loss_counter', models.IntegerField(null=True, blank=True)),
                ('l_kos_tkos', models.IntegerField(null=True, blank=True)),
                ('l_submissions', models.IntegerField(null=True, blank=True)),
                ('l_decisions', models.IntegerField(null=True, blank=True)),
                ('ufc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FighterMetric',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hasher', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('nick_name', models.CharField(max_length=300, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('reach', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('slpm', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('stracc', models.IntegerField(null=True, blank=True)),
                ('sapm', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('strdef', models.IntegerField(null=True, blank=True)),
                ('tdavg', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('tdacc', models.IntegerField(null=True, blank=True)),
                ('tddef', models.IntegerField(null=True, blank=True)),
                ('subavg', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FightMetric',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event_hasher', models.CharField(max_length=50, null=True, blank=True)),
                ('fight_hasher', models.CharField(unique=True, max_length=50)),
                ('fighter1', models.CharField(max_length=30, null=True, db_column=b'fighter1_id', blank=True)),
                ('fighter2', models.CharField(max_length=30, null=True, db_column=b'fighter2_id', blank=True)),
                ('str1', models.IntegerField(null=True, blank=True)),
                ('str2', models.IntegerField(null=True, blank=True)),
                ('td1', models.IntegerField(null=True, blank=True)),
                ('td2', models.IntegerField(null=True, blank=True)),
                ('sub1', models.IntegerField(null=True, blank=True)),
                ('sub2', models.IntegerField(null=True, blank=True)),
                ('pass1', models.IntegerField(null=True, blank=True)),
                ('pass2', models.IntegerField(null=True, blank=True)),
                ('round', models.IntegerField(null=True, blank=True)),
                ('time', models.CharField(max_length=15, null=True, blank=True)),
                ('method', models.CharField(max_length=100, null=True, blank=True)),
                ('method2', models.CharField(max_length=100, null=True, blank=True)),
                ('weight_cate', models.CharField(max_length=80, null=True, blank=True)),
            ],
        ),
    ]

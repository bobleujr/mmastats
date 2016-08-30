# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('fight_date', models.DateField()),
                ('event_id', models.IntegerField()),
                ('fight_result_type', models.CharField(max_length=50)),
                ('referee', models.CharField(max_length=150)),
                ('round', models.IntegerField()),
                ('time', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('nick_name', models.CharField(max_length=300)),
                ('birth_date', models.DateField()),
                ('locality', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=100)),
                ('height', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('weight_class', models.CharField(max_length=80)),
                ('team', models.CharField(max_length=150)),
                ('win_counter', models.IntegerField()),
                ('w_kos_tkos', models.IntegerField()),
                ('w_submissions', models.IntegerField()),
                ('w_decisions', models.IntegerField()),
                ('loss_counter', models.IntegerField()),
                ('l_kos_tkos', models.IntegerField()),
                ('l_submissions', models.IntegerField()),
                ('l_decisions', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fight',
            name='fighter1',
            field=models.ForeignKey(related_name='fighter1', to='fighterdb.Fighter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fight',
            name='fighter2',
            field=models.ForeignKey(related_name='fighter2', to='fighterdb.Fighter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fight',
            name='fighter_winner',
            field=models.ForeignKey(related_name='fighter_winner', to='fighterdb.Fighter'),
            preserve_default=True,
        ),
    ]

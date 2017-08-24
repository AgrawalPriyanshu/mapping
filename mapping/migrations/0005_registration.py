# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0004_auto_20170808_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_date', models.DateField()),
                ('comment', models.CharField(max_length=100, blank=True)),
                ('game_name', models.ManyToManyField(to='mapping.Game')),
                ('registration_id', models.ForeignKey(to='mapping.Athlete')),
            ],
        ),
    ]

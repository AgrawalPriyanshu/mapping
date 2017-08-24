# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_name', models.CharField(max_length=30)),
                ('car_number', models.CharField(default=b'True', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(default=b'True', max_length=50)),
                ('adhaar', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='Owner',
            field=models.ForeignKey(to='mapping.Person'),
        ),
    ]

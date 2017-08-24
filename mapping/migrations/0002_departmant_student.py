# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departmant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_id', models.CharField(max_length=10)),
                ('department_name', models.CharField(max_length=30)),
                ('budget', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=50)),
                ('roll_number', models.CharField(max_length=10)),
                ('allocated_department', models.ForeignKey(to='mapping.Departmant')),
            ],
        ),
    ]

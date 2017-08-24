# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_departmant_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departmant',
            new_name='Department',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20151202_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamebet',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20150920_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='result',
            field=models.TextField(default=''),
        ),
    ]

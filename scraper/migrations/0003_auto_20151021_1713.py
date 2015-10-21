# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='home_team',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='game',
            name='visit_team',
            field=models.CharField(max_length=200),
        ),
    ]

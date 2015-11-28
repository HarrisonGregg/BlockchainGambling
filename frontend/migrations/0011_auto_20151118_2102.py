# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20151021_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebet',
            name='game',
            field=models.ForeignKey(to='scraper.Game'),
        ),
    ]

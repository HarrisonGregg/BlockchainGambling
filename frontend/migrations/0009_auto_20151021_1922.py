# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20151021_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebet',
            name='game',
            field=models.ForeignKey(to='scraper.UpcomingGame'),
        ),
    ]

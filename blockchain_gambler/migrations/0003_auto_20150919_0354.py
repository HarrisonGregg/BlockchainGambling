# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain_gambler', '0002_auto_20150919_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 19, 3, 54, 52, 904086, tzinfo=utc), verbose_name=b'created time'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 19, 3, 54, 52, 904115, tzinfo=utc), verbose_name=b'last modified time'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain_gambler', '0003_auto_20150919_0354'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

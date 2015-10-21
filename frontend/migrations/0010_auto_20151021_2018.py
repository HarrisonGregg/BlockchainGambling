# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20151021_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebet',
            name='acceptor',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='acceptor'),
        ),
        migrations.AlterField(
            model_name='gamebet',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default='', related_name='creator'),
            preserve_default=False,
        ),
    ]

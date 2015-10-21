# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0007_gamebet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='result',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='user',
        ),
        migrations.AddField(
            model_name='gamebet',
            name='acceptor',
            field=models.ForeignKey(related_name='acceptor', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='gamebet',
            name='creator',
            field=models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20151021_1713'),
        ('frontend', '0006_auto_20150920_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameBet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('winner', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('game', models.ForeignKey(to='scraper.Game')),
            ],
        ),
    ]

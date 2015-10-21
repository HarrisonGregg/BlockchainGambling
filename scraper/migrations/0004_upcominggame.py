# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20151021_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingGame',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('home_team', models.CharField(max_length=200)),
                ('visit_team', models.CharField(max_length=200)),
            ],
        ),
    ]

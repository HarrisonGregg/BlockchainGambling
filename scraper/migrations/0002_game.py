# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('home_team_score', models.IntegerField()),
                ('visit_team_score', models.IntegerField()),
                ('home_team', models.ForeignKey(related_name='home_team', to='scraper.Team')),
                ('visit_team', models.ForeignKey(related_name='visit_team', to='scraper.Team')),
            ],
        ),
    ]

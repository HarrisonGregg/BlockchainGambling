# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20151202_0423'),
        ('scraper', '0004_upcominggame'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='game',
            name='visit_team_score',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='UpcomingGame',
        ),
    ]

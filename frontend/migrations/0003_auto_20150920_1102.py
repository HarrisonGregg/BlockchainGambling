# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20150920_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('credit_number', models.CharField(max_length=200)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('choice', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='bet',
            name='campaign',
            field=models.TextField(),
        ),
    ]

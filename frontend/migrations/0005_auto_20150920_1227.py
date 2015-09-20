# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('frontend', '0004_bet_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('credit_number', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to='frontend.User'),
        ),
        migrations.AlterField(
            model_name='league',
            name='admin',
            field=models.ForeignKey(to='frontend.User'),
        ),
    ]

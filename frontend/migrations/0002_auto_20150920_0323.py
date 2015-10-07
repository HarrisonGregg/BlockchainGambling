# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0001_initial'),
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='league',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='league',
            name='admin',
        ),
        migrations.AddField(
            model_name='league',
            name='admin',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='bet',
            name='league',
            field=models.ForeignKey(to='frontend.League'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

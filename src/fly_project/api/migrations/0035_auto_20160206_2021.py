# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_xplevel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedCourse',
            fields=[
            ],
            options={
                'ordering': ('created',),
                'proxy': True,
            },
            bases=('api.course',),
        ),
        migrations.CreateModel(
            name='OrderedCreditGoal',
            fields=[
            ],
            options={
                'ordering': ('-created',),
                'proxy': True,
            },
            bases=('api.creditgoal',),
        ),
        migrations.CreateModel(
            name='OrderedFinalGoal',
            fields=[
            ],
            options={
                'ordering': ('-created',),
                'proxy': True,
            },
            bases=('api.finalgoal',),
        ),
        migrations.CreateModel(
            name='OrderedQuestion',
            fields=[
            ],
            options={
                'ordering': ('num',),
                'proxy': True,
            },
            bases=('api.question',),
        ),
        migrations.CreateModel(
            name='OrderedSavingsGoal',
            fields=[
            ],
            options={
                'ordering': ('-created',),
                'proxy': True,
            },
            bases=('api.savingsgoal',),
        ),
        migrations.AlterModelOptions(
            name='creditgoal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='finalgoal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='imageupload',
            options={},
        ),
        migrations.AlterModelOptions(
            name='savingsgoal',
            options={},
        ),
    ]

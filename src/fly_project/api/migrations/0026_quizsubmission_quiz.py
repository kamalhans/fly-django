# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20160202_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsubmission',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Quiz'),
            preserve_default=False,
        ),
    ]
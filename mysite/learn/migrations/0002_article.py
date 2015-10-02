# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import learn.models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labels', learn.models.ListField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=3000)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-26 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.List'),
        ),
    ]
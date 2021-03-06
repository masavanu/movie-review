# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-07 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usereview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Usereview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('rating', jsonfield.fields.JSONField(default=[])),
                ('comments', jsonfield.fields.JSONField(default=[])),
            ],
        ),
        migrations.DeleteModel(
            name='Deployment',
        ),
    ]

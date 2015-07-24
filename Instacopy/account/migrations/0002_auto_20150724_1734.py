# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('code', models.CharField(max_length=10)),
                ('country', models.ForeignKey(to='account.Country')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='account.State'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, to='account.City', null=True),
        ),
    ]

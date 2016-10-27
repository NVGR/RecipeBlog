# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('step_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=50)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipes')),
            ],
        ),
    ]

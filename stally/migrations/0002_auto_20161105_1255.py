# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-05 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stally', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['name'], 'verbose_name': 'Pokémon', 'verbose_name_plural': 'Pokémon'},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='character',
            name='pronouns',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

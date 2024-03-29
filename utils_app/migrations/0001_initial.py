# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('Text', 'Text'), ('Video', 'Video'), ('Video/Text', 'Video/Text')], max_length=100, unique=True)),
            ],
            options={
                'db_table': 'delivery_mode',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('Greek', 'Greek'), ('English/Greek', 'English/Greek')], max_length=100, unique=True)),
            ],
            options={
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Introductory', 'Introductory'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=100, unique=True)),
            ],
            options={
                'db_table': 'course_level',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CheckBox', 'CheckBox'), ('Radio', 'Radio')], max_length=100, unique=True)),
            ],
            options={
                'db_table': 'question_type',
            },
        ),
        migrations.CreateModel(
            name='SubtitlesLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('No', 'No'), ('English', 'English'), ('Greek', 'Greek'), ('English/Greek', 'English/Greek')], max_length=100, unique=True)),
            ],
            options={
                'db_table': 'subtitles_languages',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import library_app.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('utils_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='non', max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('filename', models.FileField(max_length=2000, null=True, upload_to=library_app.models.upload_library_book)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils_app.Language')),
            ],
            options={
                'ordering': ('title',),
                'db_table': 'lib_books',
            },
        ),
        migrations.CreateModel(
            name='LibSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('title',),
                'db_table': 'lib_subject',
            },
        ),
        migrations.AddField(
            model_name='libbook',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.LibSubject'),
        ),
        migrations.AddField(
            model_name='libbook',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

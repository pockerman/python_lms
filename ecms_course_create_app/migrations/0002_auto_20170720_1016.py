# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecms_course_create_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessonquizquestion',
            options={'ordering': ('order_id',), 'verbose_name': 'Lesson Quiz Question', 'verbose_name_plural': 'Lesson Quiz Questions'},
        ),
        migrations.AddField(
            model_name='lessonquizquestion',
            name='order_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-06 22:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('collegeId', models.AutoField(primary_key=True, serialize=False)),
                ('collegeName', models.CharField(max_length=250)),
                ('isValid', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(blank=True, choices=[(None, 'Year of study'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.College'),
        ),
    ]

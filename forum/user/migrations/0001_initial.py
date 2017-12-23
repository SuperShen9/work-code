# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 07:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_code', models.CharField(max_length=100, verbose_name='激活码')),
                ('over_time', models.DateTimeField(auto_now=True, verbose_name='过期时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '激活码',
                'verbose_name_plural': '激活码',
            },
        ),
    ]
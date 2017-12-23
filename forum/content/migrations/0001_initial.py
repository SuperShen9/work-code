# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0002_auto_20171122_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('art_content', models.CharField(max_length=10000, verbose_name='文章内容')),
                ('status', models.IntegerField(choices=[(1, '常用'), (0, '待定'), (-1, '隐藏')], verbose_name='状态')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='板块索引')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
            },
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('a_key', models.AutoField(serialize=False, primary_key=True)),
                ('comp_id', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='lyric_file',
            fields=[
                ('l_key', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mp3_file',
            fields=[
                ('m_key', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('s_key', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text_description', models.TextField(max_length=1024)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mp3_file',
            name='submitted',
            field=models.ForeignKey(to='round1.Submission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lyric_file',
            name='submitted',
            field=models.ForeignKey(to='round1.Submission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='piece',
            field=models.ForeignKey(to='round1.Submission'),
            preserve_default=True,
        ),
    ]

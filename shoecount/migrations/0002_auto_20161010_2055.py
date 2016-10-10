# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoecount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('counter', models.BigIntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

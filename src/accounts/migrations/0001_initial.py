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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('A_Value', models.BooleanField(default=False)),
                ('B_Value', models.BooleanField(default=False)),
                ('C_Value', models.BooleanField(default=False)),
                ('D_Value', models.BooleanField(default=False)),
                ('Address', models.CharField(max_length=500, blank=True, null=True)),
                ('Phone', models.DecimalField(decimal_places=False, max_digits=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20180311_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('A_Value', models.BooleanField(default=False)),
                ('B_Value', models.BooleanField(default=False)),
                ('C_Value', models.BooleanField(default=False)),
                ('D_Value', models.BooleanField(default=False)),
                ('Address', models.CharField(max_length=500, blank=True, null=True)),
                ('Phone', models.DecimalField(decimal_places=False, max_digits=10)),
                ('E_Value', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

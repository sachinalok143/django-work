# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20180310_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='item_name',
            field=models.CharField(max_length=120, default=datetime.datetime(2018, 3, 11, 11, 23, 17, 157712, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

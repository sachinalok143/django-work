# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20180310_1143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='item',
            new_name='itemDetail',
        ),
    ]

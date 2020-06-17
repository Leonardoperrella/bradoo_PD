# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import bradoo.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200617_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='cnpj',
            field=models.CharField(verbose_name='CNPJ', max_length=14, unique=True, validators=[bradoo.core.validators.validate_cnpj]),
        ),
    ]

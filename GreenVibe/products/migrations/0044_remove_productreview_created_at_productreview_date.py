# Generated by Django 4.2 on 2023-12-04 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='created_at',
        ),
        migrations.AddField(
            model_name='productreview',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

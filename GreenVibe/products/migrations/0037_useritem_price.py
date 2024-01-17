# Generated by Django 4.2 on 2023-11-28 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_product_alter_useritem_product_delete_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

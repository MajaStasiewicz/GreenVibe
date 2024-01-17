# Generated by Django 4.2 on 2024-01-07 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0061_productstorage_storagejanuary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyOrderSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(unique=True)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]

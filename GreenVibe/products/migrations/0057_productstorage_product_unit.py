# Generated by Django 4.2 on 2024-01-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_unitproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstorage',
            name='product_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.unitproduct'),
        ),
    ]

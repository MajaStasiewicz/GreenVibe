# Generated by Django 4.2 on 2024-01-09 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0076_alter_newdelivery_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstorage',
            name='product_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.unitproduct'),
        ),
    ]
# Generated by Django 4.2 on 2023-11-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_flavour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='composition',
            field=models.CharField(default=0, max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default=0, max_length=2000),
        ),
    ]

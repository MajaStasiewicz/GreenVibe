# Generated by Django 4.2 on 2023-11-23 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='flavour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='product',
            name='storage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='usage',
        ),
    ]

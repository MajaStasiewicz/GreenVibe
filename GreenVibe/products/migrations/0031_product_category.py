# Generated by Django 4.2 on 2023-11-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_remove_product_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='odzywki', max_length=20),
        ),
    ]

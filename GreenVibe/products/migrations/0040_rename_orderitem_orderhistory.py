# Generated by Django 4.2 on 2023-12-02 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_remove_useritem_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderHistory',
        ),
    ]

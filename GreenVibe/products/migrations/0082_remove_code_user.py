# Generated by Django 4.2 on 2024-01-12 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0081_alter_orderhistory_delivery_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='user',
        ),
    ]
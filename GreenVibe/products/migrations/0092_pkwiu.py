# Generated by Django 4.2 on 2024-01-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0091_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PKWiU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]

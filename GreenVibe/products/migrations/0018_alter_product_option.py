# Generated by Django 4.2 on 2023-11-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='option',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
# Generated by Django 4.2 on 2024-01-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0059_orderhistory_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='delivery_status',
            field=models.CharField(choices=[('Przesłano', 'Przesłano'), ('Doręczono', 'Doręczono')], default='Przesłano', max_length=20),
        ),
    ]

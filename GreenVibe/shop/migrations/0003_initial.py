# Generated by Django 4.2 on 2023-11-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_delete_zapisne'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZapisNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]

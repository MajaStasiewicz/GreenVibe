# Generated by Django 4.2 on 2023-11-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pytania3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pytanie', models.CharField(max_length=200)),
                ('dzial', models.CharField(max_length=100)),
                ('odp1', models.CharField(max_length=100)),
                ('odp2', models.CharField(max_length=100)),
                ('odp3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pytania4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pytanie', models.CharField(max_length=200)),
                ('dzial', models.CharField(max_length=100)),
                ('odp1', models.CharField(max_length=100)),
                ('odp2', models.CharField(max_length=100)),
                ('odp3', models.CharField(max_length=100)),
                ('odp4', models.CharField(max_length=100)),
            ],
        ),
    ]
